from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .controller import observer
from m3_ext.ui import all_components as ext

class UserEditWindow(BaseEditWindow):

    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        print(self.__dict__)

        self.field__password = ext.ExtStringField(
            label="password",
            name="password",
            allow_blank=False,
            anchor="100%"
        )

        self.field__last_login = ext.ExtDateField(
            label="last login",
            name="last_login",
            format="d.m.Y",
            anchor="100%"
        )

        self.field__superuser_status = ext.ExtCheckBox(
            label="superuser status",
            name="is_superuser",
            anchor="100%"
        )

        self.field__username = ext.ExtStringField(
            label="username",
            name="username",
            allow_blank=False,
            anchor="100%"
        )

        self.field__first_name = ext.ExtStringField(
            label="first name",
            name="first_name",
            anchor="100%"
        )

        self.field__last_name = ext.ExtStringField(
            label="last name",
            name="last_name",
            anchor="100%"
        )

        self.field__email_address = ext.ExtStringField(
            label="email address",
            name="email",
            anchor="100%"
        )

        self.field__staff_status = ext.ExtCheckBox(
            label="staff status",
            name="is_staff",
            anchor="100%"
        )

        self.field__active = ext.ExtCheckBox(
            label="active",
            name="is_active",
            anchor="100%"
        )

        self.field__date_joined = ext.ExtDateField(
            label="date joined",
            name="date_joined",
            format="d.m.Y",
            anchor="100%"
        )

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email_address,
            self.field__staff_status,
            self.field__active,
            self.field__date_joined
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model)

class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = UserEditWindow

class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model)

class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(
        model, 
        field_list=["name", "content_type*", "codename"],
        model_register=observer
    )