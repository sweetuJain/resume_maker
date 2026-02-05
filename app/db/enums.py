

from sqlalchemy import Enum


user_account_status = Enum(
    "active",
    "inactive",
    "suspended",
    "blocked",
    name="user_account_status",
)

media_category = Enum(
    "profile_image",
    "resume_document",
    "certificate",
    "identity_document",
    "portfolio_asset",
    name="media_category",
)
