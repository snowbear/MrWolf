from wolf import models, views
from wolf.tests import model_mocks
from wolf.tests.views import common


class Tests(common.ViewTestBase):
    def test_can_be_rendered(self):
        model_mocks.mock_template()

        request = self.request_get('wolf:templates', [])
        views.templates(request)

    def test_template_edit_can_be_rendered(self):
        template = model_mocks.mock_template()
        request = self.request_get('wolf:template-edit', [template.id])
        views.template_edit(request, template.id)

    def test_update_template(self):
        template = model_mocks.mock_template()
        new_language = model_mocks.mock_language()
        request = self.request_post('wolf:template-edit',
                                    args=[template.id],
                                    data={
                                        'code': '2',
                                        'language_id': str(new_language.id),
                                    })
        views.template_edit(request, template.id)

        loaded_template = models.Template.objects.get(pk=template.id)
        self.assertEqual(loaded_template.code, '2')
        self.assertEqual(loaded_template.language, new_language)
