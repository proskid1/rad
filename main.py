import undetected_chromedriver as uc
from dotenv import load_dotenv
from interactionn_prim import *
from logger import Logger

load_dotenv()

# Initialize the undetected-chromedriver. It runs headless by default in recent versions
driver = uc.Chrome(headless=False)

if sys.argv.__len__() != 2:
    print(f"run this as python3 {sys.argv[0]} [account_gmail]")
    exit(1)

 # use javascript:(function(){function getXPath(el){if(el===document.body)return'/html/body';if(el.id)return"//*[@id='"+el.id+"']";var ix=0;var siblings=el.parentNode?el.parentNode.children:[];for(var i=0;i<siblings.length;i++){var sib=siblings[i];if(sib===el)return getXPath(el.parentNode)+'/'+el.tagName.toLowerCase()+'['+(ix+1)+']';if(sib.tagName===el.tagName)ix++;}return'';}let box=document.createElement('div');box.style.cssText='position:fixed;z-index:2147483647;background:rgba(20,20,20,.9);color:#fff;font:12px monospace;padding:6px 8px;border-radius:6px;pointer-events:none;';document.body.appendChild(box);let lastXpath='';document.addEventListener('mousemove',e=>{let el=e.target;if(!el||el===document) return;let xp=getXPath(el);lastXpath=xp;box.textContent=xp;box.style.left=(e.clientX+12)+'px';box.style.top=(e.clientY+12)+'px';});document.addEventListener('keydown',async e=>{if(e.key.toLowerCase()==='c'&&lastXpath){try{await navigator.clipboard.writeText(lastXpath);box.textContent='Copied! '+lastXpath;}catch(err){box.textContent='Clipboard blocked: '+lastXpath;}}});})(); to get xpath, and c to copy

try:
    logger = Logger(True)

    click_sign_in(driver, logger)

    sign_into_google(driver, logger)

    claim_daily(driver, logger)

    send_all_money_to_users(driver, os.getenv("TARGET_ACC"), logger)

    print("done")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
