# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
# import time
# def upvoat_person(username, password, target_user,Playwright,comment):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.reddit.com/")
#     time.sleep(1)
#     page.get_by_role("link", name="Log In").click()
#     time.sleep(1)
#     page.locator("input[name=\"username\"]").click()
#     time.sleep(1)
#     page.locator("input[name=\"username\"]").fill("kitdag")
#     time.sleep(1)
#     page.locator("input[name=\"username\"]").press("Tab")
#     time.sleep(1)
#     page.locator("input[name=\"password\"]").fill("Amine@13123244")
#     time.sleep(1)
#     page.locator("input[name=\"password\"]").press("Enter")
#     time.sleep(1)
#     page.goto("https://www.reddit.com/")
#     time.sleep(5)
#     page.get_by_role("textbox").click()
#     time.sleep(1)
#     page.get_by_role("textbox").fill(target_user)
#     time.sleep(1)
#     page.get_by_role("textbox").press("Enter")
#     time.sleep(3)
#     page.get_by_role("link", name="See more people").click()
#     time.sleep(2)
#     page.locator("//*[@id='main-content']/div/reddit-feed/faceplate-tracker[1]").click()
#     time.sleep(2)
#     page.get_by_role("link", name="Posts").click()
#     time.sleep(3)
#     btn = page.locator("button", has_text="Upvote").nth(0)
#     print (btn)
#     btn.click()
#     time.sleep(2)
#     # page.get_by_role("button", name="comments-action-button").nth(0).click()
#     # time.sleep(2)
#     # page.locator("button", has_text="Add a comment").nth(0).click()
#     # time.sleep(2)
#     # page.locator("#main-content").get_by_role("textbox").fill(comment)
#     # time.sleep(2)
#     # page.get_by_role("button", name="Comment", exact=True).click()
#     # time.sleep(2)
#     # page.get_by_role("button", name="Follow").click()
#     # time.sleep(2)
#     # with page.expect_popup() as page1_info:
#     #     page.get_by_label("Open chat").click()
#     # page1 = page1_info.value
#     # page1.get_by_placeholder("Message").fill("hti")
#     # page.get_by_role("link", name="Comments", exact=True).click()
#     # -----------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     upvoat_person(username="ss",password="ss",target_user="karma",Playwright=playwright,comment="comment hete")

