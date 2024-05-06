from enum import Enum
from typing import Callable, Any, Optional, List, Union, Sequence, Dict, Set, Type

from fastapi import params
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.routing import APIRoute
from fastapi.types import IncEx
from fastapi.utils import generate_unique_id
from starlette.responses import Response
from starlette.routing import BaseRoute
from starlette.requests import Request

from fastapi_msgspec.responses import MsgSpecJSONResponse
from fastapi_msgspec.requests import MSGSpecJSONRequest


class MsgSpecRoute(APIRoute):
    def __init__(
            self,
            path: str,
            endpoint: Callable[..., Any],
            *,
            response_model: Any = Default(None),
            status_code: Optional[int] = None,
            tags: Optional[List[Union[str, Enum]]] = None,
            dependencies: Optional[Sequence[params.Depends]] = None,
            summary: Optional[str] = None,
            description: Optional[str] = None,
            response_description: str = "Successful Response",
            responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
            deprecated: Optional[bool] = None,
            name: Optional[str] = None,
            methods: Optional[Union[Set[str], List[str]]] = None,
            operation_id: Optional[str] = None,
            response_model_include: Optional[IncEx] = None,
            response_model_exclude: Optional[IncEx] = None,
            response_model_by_alias: bool = True,
            response_model_exclude_unset: bool = False,
            response_model_exclude_defaults: bool = False,
            response_model_exclude_none: bool = False,
            include_in_schema: bool = True,
            response_class: Union[Type[Response], DefaultPlaceholder] = Default(
                MsgSpecJSONResponse
            ),
            dependency_overrides_provider: Optional[Any] = None,
            callbacks: Optional[List[BaseRoute]] = None,
            openapi_extra: Optional[Dict[str, Any]] = None,
            generate_unique_id_function: Union[
                Callable[["APIRoute"], str], DefaultPlaceholder
            ] = Default(generate_unique_id),
    ) -> None:
        super().__init__(
            path=path,
            endpoint=endpoint,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            name=name,
            methods=methods,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            dependency_overrides_provider=dependency_overrides_provider,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request = MSGSpecJSONRequest(request.scope, request.receive)
            return await original_route_handler(request)

        return custom_route_handler
