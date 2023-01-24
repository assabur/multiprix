from pprint import pprint

from playwright.sync_api import sync_playwright


def sosh():
    return fibre() + [] + []


def fibre():
    data = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        # context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(
            "https://shop.sosh.fr/box-internet?gclid=Cj0KCQiAlKmeBhCkARIsAHy7WVuo0gBV81VxJQFCWt6RnnvZFYirlztT_QRLPDE8sQXfiTI6hDddV_gaAuTGEALw_wcB&gclsrc=aw.ds#FIBRE"
        )
        # context.tracing.stop(path="trace.zip")

        def xp(xpath):
            return page.locator(f"xpath={xpath}").first.text_content()

        prix_promo = xp(
            '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[2]'
        )
        debit = xp('//*[@id="pills-fibre"]/div[2]/div/div[2]/div/div/div')
        prix = xp(
            '//*[@id="pills-fibre"]/div[1]/div/div/div[2]/p/span[4]/span[2]'
        )
        data.append(
            {
                "offre": f"Fibre sosh",
                "prix": prix.split()[0].replace(",", ""),
                "prix_promo": prix_promo.split()[0].replace(",", ""),
                "debit": debit.split(".")[0],
            }
        )
        context.close()
        browser.close()
    return data


if __name__ == "__main__":
    sosh()
