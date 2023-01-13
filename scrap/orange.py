from playwright.sync_api import sync_playwright
from pprint import pprint


def orange():
    return fibre() + [] + []


def fibre():
    data = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        #context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://boutique.orange.fr/internet/offres-fibre")
        #context.tracing.stop(path="trace.zip")

        def xp(xpath):
            return page.locator(f"xpath={xpath}").first.text_content()

        for i in (1, 2, 3):
            prix_promo = xp(f"//div[{i}]/section/div/div[1]/div[2]/div/p/span[1]")
            debit = xp(f"//div[{i}]/section/div/div[1]/div[1]/div/div[4]/div[1]/p/span")
            prix = xp(f"//div[{i}]/section/div/div[1]/div[2]/div/p/span[3]/span[2]")
            data.append(
                {
                    "offre": f"fibre {i} orange",
                    "prix": int(prix.split()[0].replace(",", "")),
                    "prix_promo": int(prix_promo.split()[0].replace(",", "")),
                    "debit": debit,
                }
            )
        context.close()
        browser.close()
    return data


if __name__ == "__main__":
    orange()
