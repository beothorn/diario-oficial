import re

from .base_parser import BaseParser


#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2017-10-05-ed2155_0.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-03-22-ed2275.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-04-25-ed2299.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-03-30-ed2281.pdf

class PrPontaGrossa(BaseParser):

    def bidding_exemptions(self):
        lines = self.text.splitlines()
        print(len(lines))
        exemptions_indexes = [
            index
            for index, line in enumerate(lines)
            if 'DISPENSA: Dispensa de Licitação n' in line
        ]

        sections_line_numbers = []
        for exemptions_index in exemptions_indexes:
            current_index = exemptions_index - 1
            while 'CONTRATO Nº ' not in lines[current_index]:
                current_index = current_index - 1
            sections_line_numbers.append((current_index, exemptions_index + 1))

        sections = []
        for section_interval in sections_line_numbers:
            sections.append(lines[section_interval[0]:section_interval[1]])

        sections_first_column = []
        for section in sections:
            sections_first_column.append([line[:100] for line in section])

        for s in sections_first_column:
            print("\n".join(s))
        items = [
            {
                'data': {
                    'CONTRATANTE': 'AFEPON – AGÊNCIA DE FOMENTO ECONÔMICO DE PONTA GROSSA ',
                    'CONTRATADO': 'ROSILEIDE CONCEIÇÃO GESUATO JUSTUS',
                    'OBJETO': 'Locação de 50% (cinquenta por cento) do imóvel situado na Rua Generoso Marques dos Santos, n°. 217-217A, Centro, Ponta Grossa/PR, cadastro municipal nº 36024, destinado ao armazenamento de material utilizado para prestação de serviços de iluminação e atividades operacionais.',
                    'VALOR': 'R$ 2.326,83', 
                    'DOTAÇÃO ORÇAMENTÁRIA': '201-2524-339031050000-1',
                    'BASE LEGAL': 'Artigo 24, inciso II, da Lei Federal 8.666/93.',
                },
                'source_text': '                                                 DISPENSA DE LICITAÇÃO\n     PROCESSO 001.0003845.15.0\n     CONTRATANTE: Município de Porto Alegre.\n     CONTRATADO: Classul Indústria e Comércio de Placas e Brindes Ltda.\n     OBJETO: Confecção de 50 medalhas Cidade de Porto Alegre.\n     VALOR: R$ 5.535,00.\n     DOTAÇÃO ORÇAMENTÁRIA: 201-2524-339031050000-1\n     BASE LEGAL: Artigo 24, inciso II, da Lei Federal 8.666/93.\n\n                                                  Porto Alegre, 27 de fevereiro de 2015.\n\n                                           URBANO SCHMITT, Secretário Municipal de Gestão.',
            },
            {
                'data': {
                    'CONTRATANTE': 'Município de Porto Alegre.',
                    'CONTRATADO': 'Classul Indústria e Comércio de Placas e Brindes Ltda.',
                    'OBJETO': 'Gravação a laser em 21 medalhas Cidade de Porto Alegre.',
                    'VALOR': 'R$ 735,00.',
                    'DOTAÇÃO ORÇAMENTÁRIA': '201-2524-339031050000-1',
                    'BASE LEGAL': 'Artigo 24, inciso II, da Lei Federal 8.666/93',
                },
                'source_text': '                                                 DISPENSA DE LICITAÇÃO\n     PROCESSO 001.0003844.15.3\n     CONTRATANTE: Município de Porto Alegre.\n     CONTRATADO: Classul Indústria e Comércio de Placas e Brindes Ltda.\n     OBJETO: Gravação a laser em 21 medalhas Cidade de Porto Alegre.\n     VALOR: R$ 735,00.\n     DOTAÇÃO ORÇAMENTÁRIA: 201-2524-339031050000-1\n     BASE LEGAL: Artigo 24, inciso II, da Lei Federal 8.666/93\n\n                                                  Porto Alegre, 27 de fevereiro de 2015.\n\n                                           URBANO SCHMITT, Secretário Municipal de Gestão.',
            },
            {
                'data': {
                    'CONTRATANTE': 'Município de Porto Alegre, através da Secretaria Municipal da Saúde.',
                    'CONTRATADO': 'VIP ELEVADORES LTDA',
                    'OBJETO': 'Conserto de componente eletrônico do armário de comando de elevador HMIPV, sem cobertura contratual.',
                    'VALOR': 'R$ 11.232,00 (onze mil reais, duzentos e trinta e dois reais).',
                    'BASE LEGAL': 'Artigo 24, inciso I, da Lei Federal 8.666/93',
                },
                'source_text': '                                               DISPENSA DE LICITAÇÃO\n     PROCESSO 001.037017.14.4\n     CONTRATANTE: Município de Porto Alegre, através da Secretaria Municipal da Saúde.\n     CONTRATADO: VIP ELEVADORES LTDA\n     OBJETO: Conserto de componente eletrônico do armário de comando de elevador HMIPV, sem cobertura contratual.\n     VALOR: R$ 11.232,00 (onze mil reais, duzentos e trinta e dois reais).\n     BASE LEGAL: Artigo 24, inciso I, da Lei Federal 8.666/93\n\n                                                Porto Alegre, 24 de fevereiro de 2015..\n\n                                  CARLOS HENRIQUE CASARTELLI, Secretário Municipal de Saúde.',
            },
        ]
        return items

