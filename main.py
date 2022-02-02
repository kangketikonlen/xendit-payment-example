from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.param_functions import Depends
from fastapi.staticfiles import StaticFiles

from utils.auth_util import AuthHandler
from routers import auth_route, user_route, ewallet_route, qris_route, virtacc_route, callback_route

app = FastAPI()
auth = AuthHandler()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="assets/"), name="assets")

app.include_router(
    auth_route.router,
    prefix="/auth",
    tags=["Manage Auth"]
)

app.include_router(
    user_route.router,
    prefix="/users",
    tags=["Manage Users"],
    dependencies=[Depends(auth.auth_wrapper)]
)

app.include_router(
    ewallet_route.router,
    prefix="/ewalet",
    tags=["Manage E-Wallet Payment"],
    dependencies=[Depends(auth.auth_wrapper)]
)

app.include_router(
    qris_route.router,
    prefix="/qris",
    tags=["Manage QRIS Payment"],
    # dependencies=[Depends(auth.auth_wrapper)]
)

app.include_router(
    virtacc_route.router,
    prefix="/virtual-account",
    tags=["Manage Virtual Account Payment"],
    # dependencies=[Depends(auth.auth_wrapper)]
)

app.include_router(
    callback_route.router,
    prefix="/callback",
    tags=["Manage Callback API"],
    # dependencies=[Depends(auth.auth_wrapper)]
)
