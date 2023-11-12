from fastapi_amis_admin import i18n
i18n.set_language(language='en_US')

from fastapi import FastAPI
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from datetime import date
from fastapi_scheduler import SchedulerAdmin
from fastapi.middleware.cors import CORSMiddleware
# Create `FastAPI` application
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create `AdminSite` instance
site = AdminSite(settings=Settings(database_url_async='sqlite+aiosqlite:///amisadmin.db'))

# Create an instance of the scheduled task scheduler `SchedulerAdmin`
scheduler = SchedulerAdmin.bind(site)


# Add scheduled tasks, refer to the official documentation: https://apscheduler.readthedocs.io/en/master/
# use when you want to run the job at fixed intervals of time
@scheduler.scheduled_job('interval', seconds=60)
def interval_task_test():
    print('interval task is run...')


# use when you want to run the job periodically at certain time(s) of day
@scheduler.scheduled_job('cron', hour=3, minute=30)
def cron_task_test():
    print('cron task is run...')


# use when you want to run the job just once at a certain point of time
@scheduler.scheduled_job('date', run_date=date(2022, 11, 11))
def date_task_test():
    print('date task is run...')


# Mount the background management system
site.mount_app(app)


@app.on_event("startup")
async def startup():
    # Start the scheduled task scheduler
    scheduler.start()


 
 