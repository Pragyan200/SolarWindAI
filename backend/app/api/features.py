from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.feature import FeatureResponse
from app.services.feature_engineering.feature_store_service import FeatureStoreService

router = APIRouter(
    prefix="/features",
    tags=["Features"]
)

@router.get("/", response_model=list[FeatureResponse])
def get_features(db: Session = Depends(get_db)):
    service = FeatureStoreService(db)
    return service.get_all_features()


@router.get("/{feature_id}", response_model=FeatureResponse)
def get_feature(feature_id: int, db: Session = Depends(get_db)):
    service = FeatureStoreService(db)
    return service.get_feature_by_id(feature_id)