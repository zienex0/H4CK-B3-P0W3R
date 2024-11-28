from selenium import webdriver
from teams_init_and_login import loginToTeams

def main():
    driver = webdriver.Chrome()
    email = 'sXXXXX@pjwstk.edu.pl'
    password = 'WEWILLSTOREPASSWORDSOMEWHERE'

    # login to Teams
    loginToTeams(driver=driver, email=email, password=password)


if __name__ == '__main__':
    main()
    input('Press any key to end...')


