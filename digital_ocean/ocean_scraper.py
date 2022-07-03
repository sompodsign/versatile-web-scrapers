from digital_ocean.digital_ocean_selenium import DigitalOcean

digitalOcean = DigitalOcean('https://www.digitalocean.com/community/tutorials')

for i in range(10):
    digitalOcean.click_show_more_button()

digitalOcean.get_html()
print(len(digitalOcean.get_all_tutorial_links()))

digitalOcean.close()
