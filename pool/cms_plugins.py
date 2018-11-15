from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from pool.models import SkillPluginModel
from django.utils.translation import ugettext_lazy as _


@plugin_pool.register_plugin
class SkillPlugin(CMSPluginBase):
    model = SkillPluginModel
    name = _("Skill")
    render_template = "pool/skill.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SkillPlugin, self).render(context, instance, placeholder)
        return context
