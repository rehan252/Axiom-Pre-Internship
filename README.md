# Axiom-Pre-Internship
!! Purpose of this repository is to demonstrate my work and practice during Training Courses provide by Axiom World for the Position of Python Developer !!

# Requirements 
sudo apt-get update
sudo apt-get install python3.8

# Requirements for Odoo

sudo apt-get update
sudo apt-get upgrade
sudo reboot
wget -O - https://nightly.odoo.com/odoo.key | sudo apt-key add -
echo "deb http://nightly.odoo.com/13.0/nightly/deb/ ./" | sudo tee /etc/apt/sources.list.d/odoo.list
sudo apt-get update 

sudo apt-get install postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo su - postgres
createuser odoo -U postgres -dRSP
exit

sudo apt-get install odoo
systemctl start odoo
systemctl enable odoo

You can now access Odoo using your web browser at the following address.
http://[your-vultr-instance-IP]:8069
