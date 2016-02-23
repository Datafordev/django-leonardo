# -#- coding: utf-8 -#-

from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.media.fields.folder import FolderField
from leonardo.module.web.models import ListWidget
from leonardo.module.web.widgets.forms import WidgetUpdateForm


class FolderForm(WidgetUpdateForm):

    folder = FolderField(
        help_text=_("Type to search folder or create new one."),
        add_item_link=reverse_lazy(
            'forms:create_with_form',
            kwargs={'cls_name': 'media.folder',
                    'form_cls': 'leonardo.module.media.admin.folderadmin.AddFolderPopupForm'}))


class DownloadListWidget(ListWidget):

    icon = "fa fa-list-alt"

    feincms_item_editor_form = FolderForm

    folder = models.ForeignKey('media.Folder', verbose_name=_(
        "folder"), related_name="%(app_label)s_%(class)s_folders")

    def get_items(self):
        return self.folder.media_file_files.all()

    class Meta:
        abstract = True
        verbose_name = _("download list")
        verbose_name_plural = _('download lists')
