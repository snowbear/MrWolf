from wolf import models, views
from wolf.tests.views import common

class Views_Templates_Tests(common.ViewTestBase):
    def test_can_be_rendered(self):
        template = models.Template.objects.create(code = '')
        request = self.request_get('wolf:templates', [])
        views.templates(request)

    def test_template_edit_can_be_rendered(self):
        template = models.Template.objects.create(code = '')
        request = self.request_get('wolf:template-edit', [ template.id ])
        views.template_edit(request, template.id)
        
    def test_update_template(self):
        template = models.Template.objects.create(code = '1')
        request = self.request_post('wolf:template-edit', args = [template.id ], data = { 'code': '2' })
        views.template_edit(request, template.id)
        
        loaded_template = models.Template.objects.get(pk = template.id)
        self.assertEqual(loaded_template.code, '2')
        