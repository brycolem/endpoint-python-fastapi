from sqlalchemy.ext.asyncio import AsyncSession
from app.model.application import Application
from app.model.note import Note
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

class ApplicationService:
    @staticmethod
    async def get_all_applications(db: AsyncSession):
        result = await db.execute(select(Application).options(selectinload(Application.notes)))
        applications = result.scalars().all()

        return applications

    @staticmethod
    async def get_application(db: AsyncSession, application_id: int):
        result = await db.execute(
            select(Application)
            .filter(Application.id == application_id)
            .options(selectinload(Application.notes))
        )
        application = result.scalars().first()

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        return application

    @staticmethod
    async def create_application(db: AsyncSession, application: dict):
        new_application = Application(**application)

        db.add(new_application)
        await db.commit()
        await db.refresh(new_application)

        return new_application

    @staticmethod
    async def update_application(db: AsyncSession, application_id: int, updated_application: dict):
        result = await db.execute(select(Application).filter(Application.id == application_id))
        application = result.scalars().first()

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        for key, value in updated_application.items():
            setattr(application, key, value)

        await db.commit()
        await db.refresh(application)

        return application

    @staticmethod
    async def delete_application(db: AsyncSession, application_id: int):
        result = await db.execute(select(Application).filter(Application.id == application_id))
        application = result.scalars().first()

        if not application:
            raise HTTPException(status_code=404, detail="Application not found")

        await db.delete(application)
        await db.commit()

        return {"detail": f"Application {application_id} deleted"}
