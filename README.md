# Axiom-Pre-Internship
!! Purpose of this repository is to demonstrate my work and practice during Training Courses provide by Axiom World for the Position of Python Developer !!

# Requirements 
sudo apt-get update <br/>
sudo apt-get install python3.8

# Requirements for Odoo

sudo apt-get update <br/>
sudo apt-get upgrade <br/>
sudo reboot <br/>
wget -O - https://nightly.odoo.com/odoo.key | sudo apt-key add - <br/>
echo "deb http://nightly.odoo.com/13.0/nightly/deb/ ./" | sudo tee /etc/apt/sources.list.d/odoo.list <br/>
sudo apt-get update <br/>
<br/>
sudo apt-get install postgresql <br/>
sudo systemctl start postgresql <br/>
sudo systemctl enable postgresql <br/>
sudo su - postgres <br/>
createuser odoo -U postgres -dRSP <br/>
exit <br/><br/>

sudo apt-get install odoo <br/>
systemctl start odoo <br/>
systemctl enable odoo <br/><br/>

You can now access Odoo using your web browser at the following address. <br/>
http://[your-vultr-instance-IP]:8069
