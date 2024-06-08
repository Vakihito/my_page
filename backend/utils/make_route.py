import os

main_service = "goals"
service_name = "update"
main_folder = f"/workspace/backend/src/{main_service}"

model_name = main_folder.split("/")[-1]
service_name = f"{service_name}_{model_name}"
main_service_cap = main_service.capitalize()

pathing_name = ".".join(main_folder.split("/")[2:])
pathing_name_src = ".".join(main_folder.split("/")[2:-1])

print(f"creatting new {service_name}")


def create_folder(cur_path):
    if not os.path.exists(cur_path):
        os.mkdir(cur_path)


def ext(cur_path):
    return os.path.exists(cur_path)


def create_file(cur_file_path):
    with open(cur_file_path, "w+") as f:
        f.write("")


def write_new_file(cur_file_path, new_data):
    with open(cur_file_path, "w+") as f:
        f.write(new_data)


def update_file(cur_file_path, news_str):
    with open(cur_file_path, "a") as f:
        f.write(news_str)


def add_name_to_init(init_path, file_name, object_name):
    new_import = f"from .{file_name} import {object_name}\n"
    update_file(init_path, new_import)


def case_string(s):
    words = s.split("_")
    transformed = "".join(word.capitalize() for word in words)
    return transformed


service_cased = case_string(service_name)

if not os.path.exists(main_folder):
    create_folder(f"{main_folder}/controller")
    create_file(f"{main_folder}/controller/__init__.py")
    create_folder(f"{main_folder}/factory")
    create_file(f"{main_folder}/factory/__init__.py")
    create_folder(f"{main_folder}/infra")
    create_file(f"{main_folder}/infra/__init__.py")
    create_folder(f"{main_folder}/model")
    create_file(f"{main_folder}/model/__init__.py")
    create_folder(f"{main_folder}/schema")
    create_file(f"{main_folder}/schema/__init__.py")
    create_folder(f"{main_folder}/service")
    create_file(f"{main_folder}/service/__init__.py")

########################
## create crontroller ##
########################
controller_file_content = f"""from {pathing_name}.service import {service_cased}Service
from {pathing_name}.schema import {service_cased}InputSchema, {service_cased}ResponseSchema
from starlette import status
from fastapi import APIRouter, Body, Depends


class {service_cased}Controller:
    def __init__(self, {service_name}_service: {service_cased}Service):
        self.{service_name}_service = {service_name}_service
        self.router = APIRouter()
        self.router.add_api_route(
            "/{service_name}",
            self.handle,
            methods=["POST"],
            status_code=status.HTTP_201_CREATED,
            response_model={service_cased}ResponseSchema,
            name="",
        )

    async def handle(self, {service_name}_input: {service_cased}InputSchema):
        return self.{service_name}_service.{service_name}({service_name}_input)
"""

write_new_file(
    f"{main_folder}/controller/{service_name}_controller.py", controller_file_content
)
add_name_to_init(
    f"{main_folder}/controller/__init__.py",
    f"{service_name}_controller",
    f"{service_cased}Controller",
)

####################
## create factory ##
####################
factory_file_content = f"""from fastapi import APIRouter
from {pathing_name}.service import {service_cased}Service
from {pathing_name}.controller import {service_cased}Controller
from {pathing_name}.infra import {main_service_cap}Repository
from {pathing_name_src}.shared.database_shared import get_db_session

db = next(get_db_session())


def {service_name}_router_factory() -> APIRouter:
    repository = {main_service_cap}Repository(db)
    service = {service_cased}Service(repository)
    controller = {service_cased}Controller(service)
    return controller.router
"""

write_new_file(f"{main_folder}/factory/{service_name}_factory.py", factory_file_content)
add_name_to_init(
    f"{main_folder}/factory/__init__.py",
    f"{service_name}_factory",
    f"{service_name}_router_factory",
)
