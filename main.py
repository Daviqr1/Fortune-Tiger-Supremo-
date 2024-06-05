import requests
import time
import telebot
import random 


#passo a passo 
#1 - criar um bot no telegram pelo @BotFather
#2 - adicionar o bot no grupo
#3 - descobrir o chat_id do grupo
api_key = 'insira a api do bot pelo @BotFather'
#descobrir chat_id do grupo
chat_id = 'insira o chat_id do grupo'
bot = telebot.TeleBot(api_key)
#descobrir chat_id do grupo




numero_aleatorio1 = random.randint(1,20)
numero_aleatorio2 = random.randint(1,20)
#4 - insira o seu link de afiliado
LINK_SITE = 'https://ola7k.com/yp8tkuoxg'

#5 - insira o link do grupo vip
LINK_GRUPO = 'https://t.me/MetodoCPAGRATUITO'


#6 - customize a sua mensagem
mensagem3 = f'''
✅GANHE R$10,00 DE VOLTA✅
  🎁 CASHBACK NO PIX 🎁
'''
mensagem2 = f'''
🔥CHEGA DE PERDER DINHEIRO🔥

  💸 🎁Grupo Gratuito🎁 💸 

    🚀Método CPA gratuito ✅
    🚀Video Aulas na Prática ✅
    🚀Garantido ✅
    '''

mensagem1 = f'''
✅ BRECHA IDENTIFICADA ✅

🎁 [CADASTRE-SE AQUI]({LINK_SITE}) 🎁

🐯 Fortune Tiger 🐯

🔥 {numero_aleatorio1} X NORMAL
⚡️ {numero_aleatorio2} X TURBO

⏰ VÁLIDO POR 5 MINUTOS ⏰

💸 Banca Recomendada R$10,00 💸'''





def sinal_1():
    botao = telebot.types.InlineKeyboardButton(text='CADASTRE-SE AQUI', url=LINK_SITE)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(botao)
    try:
        bot.send_message(chat_id=chat_id, text='Analisando Algoritmo...')
        print('Analisando Algoritmo...')
        time.sleep(10)
        with open('foto1.png', 'rb') as foto:
            bot.send_photo(chat_id=chat_id, photo=foto, caption=mensagem1,reply_markup=markup, parse_mode='Markdown')
        print('Sinal enviado')
    except Exception as e:
        print('Erro ao enviar mensagem1')
        print(e)
        time.sleep(1)
        sinal_1()



def sinal_2():
    botao2 = telebot.types.InlineKeyboardButton(text='SAIBA MAIS', url=LINK_GRUPO)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(botao2)
    try:
        with open('foto2.png', 'rb') as foto:
            bot.send_photo(chat_id=chat_id, photo=foto, caption=mensagem2,reply_markup=markup, parse_mode='Markdown')
        print('Carta liberada')
    except Exception as e:
        print('Erro ao enviar mensagem2')
        print(e)
        time.sleep(3)
        sinal_2()


def sinal_3():
    botao = telebot.types.InlineKeyboardButton(text='CADASTRE-SE AQUI', url=LINK_SITE)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(botao)
    try:
        with open('foto3.png', 'rb') as foto:
            bot.send_photo(chat_id=chat_id, photo=foto, caption=mensagem3, reply_markup=markup, parse_mode='Markdown')
        print('Aviso enviado')
    except Exception as e:
        print('Erro ao enviar mensagem3')
        print(e)
        time.sleep(1)
        sinal_3()







def apagar_mensagens():
    last_update_id = None
    while True:
        try:
            updates = bot.get_updates(offset=last_update_id)
            for update in updates:
                if update.message:
                    chat_id = update.message.chat.id
                    message_id = update.message.message_id
                    try:
                        bot.delete_message(chat_id=chat_id, message_id=message_id)
                        print(f'Mensagem {message_id} no chat {chat_id} apagada com sucesso.')
                    except telebot.apihelper.ApiTelegramException as e:
                        print(f'Erro ao apagar mensagem {message_id} no chat {chat_id}: {e}')
                # Atualiza o offset para a próxima chamada
                last_update_id = update.update_id + 1
            time.sleep(5)  # Espera 5 segundos antes de verificar novas atualizações
        except Exception as e:
            print('Erro ao obter atualizações')
            print(e)
            time.sleep(5)
        


def main():
    while True:
        sinal_1()
        time.sleep(5)
        sinal_2()
        time.sleep(350)
        sinal_3()
        time.sleep(20)
if __name__ == '__main__':
     main()

#gerar requirements.txt

