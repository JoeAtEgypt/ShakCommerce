from urllib.parse import urlparse

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class AppPagination(PageNumberPagination):
    page_size = 8


def get_paginated_data(
    *,
    serializer_class,
    queryset,
    request,
    pagination_class=AppPagination,
    next_api_path=None,
):
    paginator = pagination_class()

    page = paginator.paginate_queryset(
        queryset,
        request,
    )

    if page is not None:
        serializer = serializer_class(page, many=True, context={"request": request})
        response_data = paginator.get_paginated_response(serializer.data).data
        if next_api_path and response_data.get("next"):
            url = urlparse(response_data["next"])
            response_data["next"] = f"{next_api_path}?{url.query}"
        return response_data

    serializer = serializer_class(queryset, many=True, context={"request": request})

    return serializer.data
