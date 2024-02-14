#!/usr/bin/python3
from distutils.core import setup, Extension

def main():
	setup(name="fputs", version="1.0.0",
			description="A fputs function from C",
			author="Adeshina Ibrahim",
			author_email="adeshinaibrahim10@gmail.com",
			ext_modules = [Extension("fputs", ["definitions.c"])])

if __name__ == "__main__":
	main()
