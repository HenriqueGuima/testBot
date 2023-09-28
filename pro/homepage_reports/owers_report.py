    
import time
import prettytable
from selenium.webdriver.common.by import By


def owers_list(find_rows):
    # print('Counting owers')
    find_rows.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[5]/div/div/div[2]/div/table').find_elements(By.TAG_NAME, 'tr')
    table_rows = find_rows
    return table_rows

def check_pagination(chrome):
    paginationResults = chrome.find_elements(By.CLASS_NAME, 'paginate_button')
    if len(paginationResults) > 1:

        # for button in paginationResults:
        #     if "next" in button.get_attribute("class"):
        #         button.click()
        #         time.sleep(1)  

        select_results = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/label/select')
        select_results.click()
        select_max = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/label/select/option[4]')
        select_max.click()
        time.sleep(1)

        


def get_owers_name(chrome):
    owers_boxes = chrome.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[5]/div/div/div[2]/div/table').find_elements(By.TAG_NAME, 'tr')
    if not owers_boxes:
        print("owers_boxes is empty.")
        return
    
    table = prettytable.PrettyTable()
    table.field_names = ["Utente", "Total Consultas", "Consultas Dívida", "Total Dívida", "", "Edit", "Delete"]
    
    for box in owers_boxes: #row
        # print(box.text)
        columns = box.find_elements(By.TAG_NAME, 'td')
        # print([column.text for column in columns])  # Check the content of each column

        if len(columns) == 5:
            row_data = [column.text for column in columns]
            # table.add_row(row_data)
            actions_link = columns[4].find_elements(By.TAG_NAME, 'a')
            link_data = [link.get_attribute("href") for link in actions_link]

            table.add_row(row_data + link_data)
            # for link in actions_link:
            #     has_link = link.get_attribute("href")
            #     print(has_link)

        # else:
            # print(f"Skipping row with unexpected number of columns: {len(columns)}")
              
    print(table)
