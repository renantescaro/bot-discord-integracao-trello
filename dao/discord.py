class DiscordDao:
    def dividir_str_para_mensagem(self, texto_completo):
        texto = texto_completo
        lista_textos = []
        while (len(texto) > 0):
            if len(texto) > 2000:
                lista_textos.append(texto[0:1999])
                if len(texto) > 4000:
                    texto = texto[1999:4000]
                else:
                    texto = texto[1999:len(texto)]
            else:
                lista_textos.append(texto[0:len(texto)])
                texto = ''
        return lista_textos