from fastapi import Depends, HTTPException, Cookie, status
from typing_extensions import Annotated


def check_user_cookie(user: Annotated[str, Cookie()]):
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cookie for user is not set")