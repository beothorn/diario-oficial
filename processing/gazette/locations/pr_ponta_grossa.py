import re

from .base_parser import BaseParser


#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2017-10-05-ed2155_0.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-03-22-ed2275.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-04-25-ed2299.pdf
#http://www.pontagrossa.pr.gov.br/files/diario-oficial/2018-03-30-ed2281.pdf

class PrPontaGrossa(BaseParser):

    #TODO: metodo que faz a regex e retorna o primeiro grupo e faz trim ou retorna vazio

    def bidding_exemptions(self):
        lines = self.text.splitlines()
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

        sections_one_line = []

        for s in sections_first_column:
            section_one_line = "".join(s)
            section_one_line = re.sub(' +',' ',section_one_line)
            sections_one_line.append(section_one_line)


        items = []

        for l in sections_one_line:

            valor = re.search('VALOR:(.*)PRAZO:', l).group(1).strip()

            items.append(
                {
                    'data' : {
                        'CONTRATANTE':re.search('LOCATÁRIO:(.*)LOCADOR:', l).group(1).strip(),
                        'CONTRATADO':re.search('LOCADOR:(.*)OBJETO:', l).group(1).strip(),
                        'OBJETO':re.search('OBJETO:(.*)VALOR:', l).group(1).strip(),
                        'VALOR':re.search('R\$ ([\d.]+,\d{2})', valor).group(1).strip(), 
                        'DOTAÇÃO ORÇAMENTÁRIA':'na',
                        'BASE LEGAL':'na'
                    },
                    'source_text':l
                }
            )

        return items
