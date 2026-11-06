from fastapi import APIRouter

from ..models.recommendation import Recommendation

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

RECOMMENDATIONS = [
    Recommendation(id=1, text="Find store hours, including holiday hours"),
    Recommendation(id=2, text="Look up an order or delivery status"),
    Recommendation(id=3, text="Explain the return and exchange policy"),
]


@router.get("")
async def get_recommendations() -> list[Recommendation]:
    return RECOMMENDATIONS
