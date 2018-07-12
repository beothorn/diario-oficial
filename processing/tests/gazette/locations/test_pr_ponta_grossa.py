from unittest import TestCase

from gazette.locations.pr_ponta_grossa import PrPontaGrossa


class TestPrPontaGrossa(TestCase):

    def setUp(self):
        path = 'tests/gazette/fixtures/pr_ponta_grossa.txt'
        with open(path) as file:
            self.text = file.read()
        self.subject = PrPontaGrossa(self.text)

    #def test_pages(self):
    #    pages = self.subject.pages()
    #    self.assertEqual(19, len(pages))
    #    self.assertEqual(self.text[:3498], pages[0].strip())

    def test_bidding_exemptions(self):
        exemptions = self.subject.bidding_exemptions()
        expectation = [
            {
                'data': {
                    'CONTRATANTE':'AFEPON – AGÊNCIA DE FOMENTO ECONÔMICO DE PONTA GROSSA',
                    'CONTRATADO':'ROSILEIDE CONCEIÇÃO GESUATO JUSTUS',
                    'OBJETO':'Locação de 50% (cinquenta por cento) do imóvel situado na Rua Generoso Marques dos Santos, n°. 217-217A, Centro, Ponta Grossa/PR, cadastro municipal nº 36024, destinado ao armazenamento de material utilizado para prestação de serviços de iluminação e atividadesoperacionais.',
                    'VALOR':'2.326,83', 
                    'DOTAÇÃO ORÇAMENTÁRIA':'na',
                    'BASE LEGAL':'na'
                },
                'source_text': ' CONTRATO Nº 004/2018 LOCATÁRIO: AFEPON – AGÊNCIA DE FOMENTO ECONÔMICO DE PONTA GROSSA LOCADOR: ROSILEIDE CONCEIÇÃO GESUATO JUSTUS OBJETO: Locação de 50% (cinquenta por cento) do imóvel situado na Rua Generoso Marques dos Santos, n°. 217-217A, Centro, Ponta Grossa/PR, cadastro municipal nº 36024, destinado ao armazenamento de material utilizado para prestação de serviços de iluminação e atividadesoperacionais. VALOR: R$ 2.326,83 (dois mil trezentos e vinte seis reais e oitenta e três centavos) mensais. PRAZO: início em 26/05/2018 e término em 26/05/2019. FORO: Comarca de Ponta Grossa, Estado do Paraná. DISPENSA: Dispensa de Licitação n° 4/2018. ',
            },
            {
                'data': {
                    'CONTRATANTE':'AFEPON – AGÊNCIA DE FOMENTO ECONÔMICO DE PONTA GROSSA',
                    'CONTRATADO':'MARIA ROSALY GESUATO THOMAZ',
                    'OBJETO':'Locação de 50% (cinquenta por cento) do imóvel situado na Rua Generoso Marques dos Santos, n°. 217-217A, Centro, Ponta Grossa/PR, cadastro municipal nº 36024, destinado ao armazenamento de material utilizado para prestação de serviços de iluminação e atividadesoperacionais.',
                    'VALOR':'', 
                    'DOTAÇÃO ORÇAMENTÁRIA':'na',
                    'BASE LEGAL':'na'
                },
                'source_text': ' CONTRATO Nº 005/2018 LOCATÁRIO: AFEPON – AGÊNCIA DE FOMENTO ECONÔMICO DE PONTA GROSSA LOCADOR: MARIA ROSALY GESUATO THOMAZ OBJETO: Locação de 50% (cinquenta por cento) do imóvel situado na Rua Generoso Marques dos Santos, n°. 217-217A, Centro, Ponta Grossa/PR, cadastro municipal nº 36024, destinado ao armazenamento de material utilizado para prestação de serviços de iluminação e atividadesoperacionais. VALOR: início em 26/05/2018 e término em 26/05/2019. PRAZO: R$ 2.326,83 (dois mil trezentos e vinte seis reais e oitenta e três centavos) mensais. FORO: Comarca de Ponta Grossa, Estado do Paraná. DISPENSA: Dispensa de Licitação n° 4/2018. ',
            },
        ]
        self.assertEqual(expectation, exemptions)
