from setuptools import setup

setup(
	name="ftrans",
	version="1.0",
	license="https://www.gnu.org/licenses/gpl-3.0.txt",
	description="A simple file transfor tool for LAN",
	author="Zumium",
	author_email="martin007323@gmail.com",
	packages=['ftrans'],
	package_data={
		'ftrans':['README.md','LICENSE','DESIGN','LICENSE-HEADER']
	},
	install_requires=[],
	entry_points="""
	[console_scripts]
	ftrans=ftrans.main:main
	""",
)
