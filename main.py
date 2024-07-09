import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")



def Start(update, context):
    update.message.reply_text("""Hello! Welcome to  StudysyncBot.
    Click the /help to choose your group.""")

def helps(update, context):
    update.message.reply_text(
    """
    Hi there! I'm Learnix created by Dinosaurs. Choose Your Group:-

    /ComputerScience - To get your course materials
    /Biomaths - To get your course materials
        
    I Hope this helps :)
    
    """
    )

def Biomaths(update, context):
    update.message.reply_text(
    """
    /Biology - To get the Important questions and Question papers
    Common Subjects => To get /Physics,/Chemistry,/Maths,/Tamil,/English
    
    """ 
    )

def Biology(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1ghyz5Bivz2oePK7XUNhfPwRWIemuPhwm/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1x-YTi3UP64_mDrOl5lQd9vlQrObgGiXo?usp=drive_link
    """ 
    )

def CSmaterial(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1XJ_oQOcK0h4EYy9df9dIqG-K3r9rPoJq/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1II2LWQwaLgVtosdXagI7-S7l79YpJ07Z?usp=drive_link
    """ 
    )

def ComputerScience(update, context):
    update.message.reply_text(
    """
    /CSmaterial - To get the Important questions and Question papers 
    Common Subjects => To get /Physics,/Chemistry,/Maths,/Tamil,/English
    
    """ 
    )    
def CSmaterial(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1XJ_oQOcK0h4EYy9df9dIqG-K3r9rPoJq/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1II2LWQwaLgVtosdXagI7-S7l79YpJ07Z?usp=drive_link
    """ 
    )

def Physics(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1G8e3ky4iQkDI6rgCDpVvAJvUkOT0TDy2/view?usp=drive_link
    Important problems => https://drive.google.com/file/d/1RiNYeRU-alRrKoblnU2SVEmRffCCpKeS/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1lFVxuld5daNV153Qrn8ziy_kmKKNf-tM?usp=drive_link
    """
    )

def Chemistry(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1Sj4_kjPYoBIocIV2MXWvoLEN4V5RIj4L/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1ZqBufZ_tuG7WAeqQ3xO1XffOhPj7xGrG?usp=drive_link
    """
    )

def Maths(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1INwug_TRGoZ4v3IUMsR0OQ1hyZMoTFT1/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1ZbDmOpoAYajaxqgnIX5Hbo31ARd98DZc?usp=drive_link
    """
    )
def Tamil(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1gv90Wt1VU5fyfrCp_rhqkFRL-MxZTmHF/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/1nK0wpSxGr9oFVsk04bHe7_tIaJfPq9aM?usp=drive_link
    """
    )

def English(update, context):
    update.message.reply_text(
    """
    Important Questions => https://drive.google.com/file/d/1Q76ZODnxuzDIMUl_eINrJK_l9ZM_MgOf/view?usp=drive_link
    Previous Year Questions => https://drive.google.com/drive/folders/16XblqR-NzPOkxupeqFaIzUvnTUxo9Msc?usp=drive_link
    """
    )

updater = telegram.ext.Updater(TOKEN, use_context = True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', Start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('computerscience', ComputerScience))
dispatch.add_handler(telegram.ext.CommandHandler('CSmaterial', CSmaterial))
dispatch.add_handler(telegram.ext.CommandHandler('Physics',Physics))
dispatch.add_handler(telegram.ext.CommandHandler('Chemistry',Chemistry))

dispatch.add_handler(telegram.ext.CommandHandler('Maths',Maths))
dispatch.add_handler(telegram.ext.CommandHandler('English',English))
dispatch.add_handler(telegram.ext.CommandHandler('Tamil',Tamil))
dispatch.add_handler(telegram.ext.CommandHandler('Biomaths',Biomaths))
dispatch.add_handler(telegram.ext.CommandHandler('Biology',Biology))

updater.start_polling()
updater.idle()