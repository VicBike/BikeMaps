# Generated by Django 3.1.7 on 2023-01-15 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='age',
            field=models.CharField(blank=True, choices=[('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'), ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'), ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'), ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'), ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'), ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'), ('1949', '1949'), ('1948', '1948'), ('1947', '1947'), ('1946', '1946'), ('1945', '1945'), ('1944', '1944'), ('1943', '1943'), ('1942', '1942'), ('1941', '1941'), ('1940', '1940'), ('1939', '1939'), ('1938', '1938'), ('1937', '1937'), ('1936', '1936'), ('1935', '1935'), ('1934', '1934'), ('1933', '1933'), ('1932', '1932'), ('1931', '1931'), ('1930', '1930'), ('1929', '1929'), ('1928', '1928'), ('1927', '1927'), ('1926', '1926'), ('1925', '1925'), ('1924', '1924'), ('1923', '1923'), ('1922', '1922'), ('1921', '1921'), ('1920', '1920'), ('1919', '1919'), ('1918', '1918'), ('1917', '1917'), ('1916', '1916'), ('1915', '1915'), ('1914', '1914'), ('1913', '1913'), ('1912', '1912'), ('1911', '1911')], max_length=15, null=True, verbose_name='What is your birth year?'),
        ),
    ]
