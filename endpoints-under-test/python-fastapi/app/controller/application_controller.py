from fastapi import APIRouter, Depends
from typing import AsyncGenerator
from app.service.application_service import ApplicationService
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import SessionLocal

router = APIRouter()

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        try:
            yield db
        except Exception as e:
            print(f"Error during DB session: {e}")
            await db.rollback()
            raise
        finally:
            await db.close()

@router.get("/application")
async def get_all_applications(db: AsyncSession = Depends(get_db)):
    return await ApplicationService.get_all_applications(db)

@router.get("/application/{application_id}")
async def get_application(application_id: int, db: AsyncSession = Depends(get_db)):
    return await ApplicationService.get_application(db, application_id)

@router.post("/application")
async def create_application(application: dict, db: AsyncSession = Depends(get_db)):
    return await ApplicationService.create_application(db, application)

@router.put("/application/{application_id}")
async def update_application(application_id: int, updated_application: dict, db: AsyncSession = Depends(get_db)):
    return await ApplicationService.update_application(db, application_id, updated_application)

@router.delete("/application/{application_id}")
async def delete_application(application_id: int, db: AsyncSession = Depends(get_db)):
    return await ApplicationService.delete_application(db, application_id)
