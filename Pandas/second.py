import pandas as pd
import numpy as np

print("=" * 60)
print("SECTION 1: CREATION & I/O")
print("=" * 60)

# pd.DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# pd.Series
s = pd.Series([10, 20, 30])

# pd.read_csv
df_csv = pd.read_csv('file.csv')

# pd.read_excel
df_excel = pd.read_excel('file.xlsx')

# pd.read_json
df_json = pd.read_json('file.json')

# pd.read_sql
df_sql = pd.read_sql("SELECT * FROM table", con=engine)

# pd.read_html
tables = pd.read_html('page.html')

# pd.read_clipboard
df = pd.read_clipboard()

# pd.read_parquet
df = pd.read_parquet('file.parquet')

# pd.read_feather
df = pd.read_feather('file.feather')

# pd.read_hdf
df = pd.read_hdf('file.h5')

# pd.read_sas
df = pd.read_sas('file.sas7bdat')

# pd.read_stata
df = pd.read_stata('file.dta')

# pd.read_spss
df = pd.read_spss('file.sav')

# pd.read_fwf
df = pd.read_fwf('file.txt')

# pd.read_orc
df = pd.read_orc('file.orc')

# pd.read_pickle
df = pd.read_pickle('file.pkl')

# pd.read_gbq
df = pd.read_gbq(query, project_id)

# pd.read_table
df = pd.read_table('file.tsv', sep='\t')

# pd.DataFrame.from_dict
df = pd.DataFrame.from_dict({'A': [1, 2]})

# pd.DataFrame.from_records
df = pd.DataFrame.from_records(data, index)

# pd.read_xml
df = pd.read_xml('file.xml')

print("\nSECTION 2: INSPECTION")

# df.head()
df.head()

# df.tail()
df.tail()

# df.sample()
df.sample(n=3)

# df.describe()
df.describe()

# df.info()
df.info()

# df.shape
print(df.shape)

# df.size
print(df.size)

# df.ndim
print(df.ndim)

# df.dtypes
print(df.dtypes)

# df.columns
print(df.columns)

# df.index
print(df.index)

# df.values
print(df.values)

# df.axes
print(df.axes)

# df.empty
print(df.empty)

# df.isna()
df.isna()

# df.isnull()
df.isnull()

# df.notna()
df.notna()

# df.notnull()
df.notnull()

# df.count()
df.count()

# df.nunique()
df.nunique()

# df.unique()
df['col'].unique()

# df.value_counts()
df.value_counts()

# df.memory_usage()
df.memory_usage()

# df.duplicated()
df.duplicated()

# df.duplicated().sum()
df.duplicated().sum()

print("\nSECTION 3: SELECTION & INDEXING")

# df['col']
df['col']

# df[['col1', 'col2']]
df[['col1', 'col2']]

# df.iloc[]
df.iloc[0]

# df.iloc[:, 1]
df.iloc[:, 1]

# df.loc[]
df.loc[0]

# df.loc[:, 'col']
df.loc[:, 'col']

# df.at[]
df.at[0, 'col']

# df.iat[]
df.iat[0, 1]

# df.filter()
df.filter(items=['col1', 'col2'])

# df.filter(regex='^A')
df.filter(regex='^A')

# df.where()
df.where(df > 0)

# df.mask()
df.mask(df > 0, 0)

# df.query()
df.query('col > 5')

# df.xs()
df.xs(key='value')

# df.get()
df.get('col')

# df.pop()
df.pop('col')

print("\nSECTION 4: FILTERING")

# df[df['col'] > 0]
df[df['col'] > 0]

# df[(df['a'] > 0) & (df['b'] < 10)]
df[(df['a'] > 0) & (df['b'] < 10)]

# df[df['col'].isin([1, 2, 3])]
df[df['col'].isin([1, 2, 3])]

# df[~df['col'].isin([1, 2, 3])]
df[~df['col'].isin([1, 2, 3])]

# df[df['col'].between(1, 5)]
df[df['col'].between(1, 5)]

# df[df['col'].str.contains('pattern')]
df[df['col'].str.contains('pattern')]

# df[df['col'].str.startswith('A')]
df[df['col'].str.startswith('A')]

# df[df['col'].str.endswith('z')]
df[df['col'].str.endswith('z')]

# df[df['col'].str.match(r'^A')]
df[df['col'].str.match(r'^A')]

# df[df['col'].str.isdigit()]
df[df['col'].str.isdigit()]

print("\nSECTION 5: SORTING & ORDERING")

# df.sort_values()
df.sort_values(by='col')

# df.sort_values(ascending=False)
df.sort_values(by='col', ascending=False)

# df.sort_index()
df.sort_index()

# df.nlargest()
df.nlargest(3, 'col')

# df.nsmallest()
df.nsmallest(3, 'col')

# df.rank()
df['col'].rank()

print("\nSECTION 6: ADDING / MODIFYING COLUMNS")

# df['new_col'] = ...
df['new_col'] = [1, 2, 3, 4]

# df.assign()
df = df.assign(new_col=lambda x: x['A'] * 2)

# df.eval()
df.eval('Sum = A + B')

# df.assign()
df.assign(Diff=lambda x: x['A'] - x['B'])

# df.insert()
df.insert(loc=2, column='new_col', value=[1, 2, 3])

print("\nSECTION 7: DROPPING")

# df.drop()
df.drop(columns='col')

# df.drop(index=0)
df.drop(index=0)

# df.drop_duplicates()
df.drop_duplicates()

# df.dropna()
df.dropna()

# df.dropna(subset=['col'])
df.dropna(subset=['col'])

print("\nSECTION 8: HANDLING MISSING DATA")

# df.fillna()
df.fillna(0)

# df.fillna(method='ffill')
df.fillna(method='ffill')

# df.fillna(method='bfill')
df.fillna(method='bfill')

# df.replace()
df.replace({0: 100})

# df.interpolate()
df.interpolate()

# df.ffill()
df.ffill()

# df.bfill()
df.bfill()

print("\nSECTION 9: STATISTICAL METHODS")

# df.mean()
df.mean()

# df.median()
df.median()

# df.mode()
df.mode()

# df.std()
df.std()

# df.var()
df.var()

# df.min()
df.min()

# df.max()
df.max()

# df.sum()
df.sum()

# df.product()
df.product()

# df.cumsum()
df.cumsum()

# df.cumprod()
df.cumprod()

# df.cummin()
df.cummin()

# df.cummax()
df.cummax()

# df.quantile()
df.quantile(0.25)

# df.kurt()
df.kurt()

# df.sem()
df.sem()

# df.skew()
df.skew()

# df.abs()
df.abs()

# df.clip()
df.clip(lower=0, upper=10)

# df.corr()
df.corr()

# df.cov()
df.cov()

# df.corrwith()
df.corrwith(df2)

# df.describe()
df.describe()

# df.idxmax()
df.idxmax()

# df.idxmin()
df.idxmin()

# df.mad()
df.mad()

# df.nsmallest() - also in sorting
df.nsmallest(3, 'col')

# df.nlargest() - also in sorting
df.nlargest(3, 'col')

print("\nSECTION 10: GROUPBY & AGGREGATION")

# df.groupby()
df.groupby('col')

# df.groupby().sum()
df.groupby('col').sum()

# df.groupby().mean()
df.groupby('col').mean()

# df.groupby().count()
df.groupby('col').count()

# df.groupby().size()
df.groupby('col').size()

# df.groupby().max()
df.groupby('col').max()

# df.groupby().min()
df.groupby('col').min()

# df.groupby().std()
df.groupby('col').std()

# df.groupby().var()
df.groupby('col').var()

# df.groupby().agg()
df.groupby('col').agg('sum')

# df.groupby().agg(['sum', 'mean'])
df.groupby('col').agg(['sum', 'mean'])

# df.groupby().agg({'a': 'sum', 'b': 'mean'})
df.groupby('col').agg({'a': 'sum', 'b': 'mean'})

# df.groupby().transform()
df.groupby('col').transform('sum')

# df.groupby().filter()
df.groupby('col').filter(lambda x: len(x) > 1)

# df.groupby().apply()
df.groupby('col').apply(lambda x: x.sum())

# df.groupby().first()
df.groupby('col').first()

# df.groupby().last()
df.groupby('col').last()

# df.groupby().nth()
df.groupby('col').nth(0)

# df.groupby().pct_change()
df.groupby('col').pct_change()

# s.groupby() - for Series
s.groupby(df['col']).sum()

# pd.Grouper
df.groupby(pd.Grouper(key='date', freq='M'))

print("\nSECTION 11: PIVOT & RESHAPE")

# df.pivot()
df.pivot(index='id', columns='cat', values='val')

# df.pivot_table()
df.pivot_table(values='val', index='id', columns='cat', aggfunc='sum')

# df.stack()
df.stack()

# df.unstack()
df.unstack()

# df.melt()
df.melt(id_vars='id', value_vars=['a', 'b'])

# pd.crosstab
pd.crosstab(df['col1'], df['col2'])

# df.explode()
df.explode('list_col')

print("\nSECTION 12: MERGE / JOIN / CONCATENATE")

# pd.concat()
pd.concat([df1, df2])

# pd.concat(axis=1)
pd.concat([df1, df2], axis=1)

# df.merge()
df1.merge(df2, on='key')

# df.merge(how='left')
df1.merge(df2, on='key', how='left')

# df.join()
df1.join(df2)

# df.join(how='inner')
df1.join(df2, how='inner')

pd.merge(df1, df2, on='key')
pd.merge(df1, df2, left_on='lkey', right_on='rkey')

print("\nSECTION 13: COMBINING / COMPARING")

# df.append() – deprecated (use pd.concat)
# Deprecated: df.append
# Use: pd.concat([df, new_row])

# df.update() – updates values
df.update(other_df)

# df.combine_first()
df.combine_first(other_df)

# df.equals()
df.equals(other_df)

pd.concat([df, other_df], ignore_index=True)

print("\nSECTION 14: APPLY & MAP")

# df.apply()
df.apply(func, axis=0)

# df.apply(func, axis=1)
df.apply(func, axis=1)

# s.apply()
s.apply(func)

# df.applymap()
df.applymap(func)

# df.map()
df['col'].map({1: 'one', 2: 'two'})

# s.map()
s.map(lambda x: x * 2)

# df.transform()
df.transform(func)

print("\nSECTION 15: STRING OPERATIONS")

# df['col'].str.upper()
df['col'].str.upper()

# df['col'].str.lower()
df['col'].str.lower()

# df['col'].str.len()
df['col'].str.len()

# df['col'].str.contains()
df['col'].str.contains('pattern')

# df['col'].str.replace()
df['col'].str.replace('old', 'new')

# df['col'].str.split()
df['col'].str.split(',')

# df['col'].str.strip()
df['col'].str.strip()

# df['col'].str.join()
df['col'].str.join(',')

# df['col'].str.slice()
df['col'].str.slice(0, 3)

# df['col'].str.startswith()
df['col'].str.startswith('A')

# df['col'].str.endswith()
df['col'].str.endswith('z')

# df['col'].str.extract()
df['col'].str.extract(r'(\d+)')

# df['col'].str.findall()
df['col'].str.findall(r'\d+')

# df['col'].str.title()
df['col'].str.title()

# df['col'].str.capitalize()
df['col'].str.capitalize()

# df['col'].str.zfill()
df['col'].str.zfill(5)

# df['col'].str.pad()
df['col'].str.pad(width=10)

# df['col'].str.center()
df['col'].str.center(10)

# df['col'].str.ljust()
df['col'].str.ljust(10)

# df['col'].str.rjust()
df['col'].str.rjust(10)

# df['col'].str.wrap()
df['col'].str.wrap(10)

# df['col'].str.encode()
df['col'].str.encode('utf-8')

# df['col'].str.normalize()
df['col'].str.normalize(form='NFC')

print("\nSECTION 16: DATETIME OPERATIONS")

# pd.to_datetime()
pd.to_datetime('2024-01-01')

# pd.to_timedelta()
pd.to_timedelta(1, unit='D')

# pd.date_range()
pd.date_range(start='2024-01-01', periods=5, freq='D')

# pd.timedelta_range()
pd.timedelta_range(start='1 day', periods=5)

# pd.DatetimeIndex
pd.DatetimeIndex(['2024-01-01', '2024-01-02'])

# pd.PeriodIndex
pd.PeriodIndex(['2024-01', '2024-02'], freq='M')

# pd.Timestamp
pd.Timestamp('2024-01-01')

# pd.Timedelta
pd.Timedelta('1 day')

# df['col'].dt.year
df['col'].dt.year

# df['col'].dt.month
df['col'].dt.month

# df['col'].dt.day
df['col'].dt.day

# df['col'].dt.hour / minute / second / microsecond / nanosecond
df['col'].dt.hour

# df['col'].dt.dayofweek
df['col'].dt.dayofweek

# df['col'].dt.day_name()
df['col'].dt.day_name()

# df['col'].dt.month_name()
df['col'].dt.month_name()

# df['col'].dt.weekday
df['col'].dt.weekday

# df['col'].dt.weekofyear / isocalendar().week
df['col'].dt.isocalendar().week

# df['col'].dt.quarter
df['col'].dt.quarter

# df['col'].dt.is_leap_year
df['col'].dt.is_leap_year

# df['col'].dt.date
df['col'].dt.date

# df['col'].dt.time
df['col'].dt.time

# df['col'].dt.tz_localize()
df['col'].dt.tz_localize('UTC')

# df['col'].dt.tz_convert()
df['col'].dt.tz_convert('US/Eastern')

# df['col'].dt.floor()
df['col'].dt.floor('D')

# df['col'].dt.ceil()
df['col'].dt.ceil('D')

# df['col'].dt.round()
df['col'].dt.round('D')

# df['col'].dt.normalize()
df['col'].dt.normalize()

# df['col'].dt.strftime()
df['col'].dt.strftime('%Y-%m-%d')

# df['col'].dt.total_seconds()
df['col'].dt.total_seconds()

# df['col'].dt.days
df['col'].dt.days

# df['col'].dt.seconds
df['col'].dt.seconds

# df['col'].dt.microseconds
df['col'].dt.microseconds

print("\nSECTION 17: RESAMPLING & WINDOW")

# df.resample()
df.resample('D').sum()

# df.rolling()
df.rolling(window=3).sum()

# df.expanding()
df.expanding().mean()

# df.ewm()
df.ewm(span=3).mean()

# df.rolling().corr()
df.rolling(3).corr()

# df.rolling().cov()
df.rolling(3).cov()

# df.rolling().var()
df.rolling(3).var()

# df.rolling().min()
df.rolling(3).min()

# df.rolling().max()
df.rolling(3).max()

# df.rolling().std()
df.rolling(3).std()

# df.rolling().mean()
df.rolling(3).mean()

# df.rolling().median()
df.rolling(3).median()

# df.rolling().skew()
df.rolling(3).skew()

# df.rolling().kurt()
df.rolling(3).kurt()

# df.rolling().quantile()
df.rolling(3).quantile(0.5)

# df.rolling().apply()
df.rolling(3).apply(np.mean)

# df.expanding().sum()
df.expanding().sum()

# df.expanding().mean()
df.expanding().mean()

# df.expanding().min()
df.expanding().min()

# df.expanding().max()
df.expanding().max()

# df.ewm().sum()
df.ewm(span=5).sum()

# df.ewm().mean()
df.ewm(span=5).mean()

# df.shift()
df.shift(periods=1)

# df.diff()
df.diff()

# df.pct_change()
df.pct_change()

print("\nSECTION 18: ADDING & REMOVING ROWS")

# df.loc[len(df)] = ...
df.loc[len(df)] = [1, 2, 3]

# df.append() – deprecated
# df.append(new_row, ignore_index=True)
# Use: pd.concat instead

# df.concat() – rows
pd.concat([df, new_df], ignore_index=True)

# df.drop()
df.drop(index=0)

# df.drop_duplicates()
df.drop_duplicates()

print("\nSECTION 19: INDEX & COLUMN MANAGEMENT")

# df.set_index()
df.set_index('column_name')

# df.reset_index()
df.reset_index()

# df.rename()
df.rename(columns={'old': 'new'}, inplace=True)

# df.columns = [...]
df.columns = ['A', 'B', 'C']

# df.index.names
df.index.names

# df.set_axis()
df.set_axis(['a', 'b'], axis=1)

# df.reindex()
df.reindex([0, 1, 2, 3])

# df.reindex(columns=new_cols)
df.reindex(columns=['col1', 'col2'])

# pd.MultiIndex.from_arrays
idx = pd.MultiIndex.from_arrays([[1, 1, 2, 2], ['a', 'b', 'a', 'b']], names=['first', 'second'])
pd.DataFrame(np.random.randn(4, 2), index=idx)

# pd.MultiIndex.from_tuples
pd.MultiIndex.from_tuples([(1, 'a'), (1, 'b')])

# pd.MultiIndex.from_product
pd.MultiIndex.from_product([[1, 2], ['a', 'b']], names=['num', 'letter'])

# df.stack() / unstack() — also reshaping
df.stack()
df.unstack()

# df.swaplevel()
df.swaplevel(0, 1)

# df.sort_index(level=0)
df.sort_index(level=0)

# df.xs() — cross-section
df.xs(key=1, level='first')

print("\nSECTION 20: CATEGORICAL DATA")

# pd.Categorical
pd.Categorical(['a', 'b', 'c', 'a'])

# df.astype('category')
df['col'].astype('category')

# df['col'].cat.categories
df['col'].cat.categories

# df['col'].cat.codes
df['col'].cat.codes

# df['col'].cat.add_categories()
df['col'].cat.add_categories('d')

# df['col'].cat.remove_categories()
df['col'].cat.remove_categories('a')

# df['col'].cat.set_categories()
df['col'].cat.set_categories(['a', 'b', 'c'])

# df['col'].cat.rename_categories()
df['col'].cat.rename_categories({'a': 'A'})

# df['col'].cat.reorder_categories()
df['col'].cat.reorder_categories(['a', 'b', 'c'])

# df['col'].cat.remove_unused_categories()
df['col'].cat.remove_unused_categories()

# df['col'].cat.remove_na_categories()
df['col'].cat.remove_unused_categories()

# df.corrwith() — also in stats
df.corrwith(other)

print("\nSECTION 21: COPYING & DUPLICATING")

# df.copy()
df.copy()

# df.copy(deep=True)
df.copy(deep=True)

print("\nSECTION 22: EXPORT / SAVE")

# df.to_csv()
df.to_csv('output.csv')

# df.to_csv(index=False)
df.to_csv('output.csv', index=False)

# df.to_excel()
df.to_excel('output.xlsx')

# df.to_json()
df.to_json('output.json')

# df.to_sql()
df.to_sql('table_name', con=engine)

# df.to_html()
df.to_html('output.html')

# df.to_parquet()
df.to_parquet('output.parquet')

# df.to_feather()
df.to_feather('output.feather')

# df.to_hdf()
df.to_hdf('output.h5', key='df', mode='w')

# df.to_pickle()
df.to_pickle('output.pkl')

# df.to_stata()
df.to_stata('output.dta')

# df.to_sas()
df.to_sas('output.sas7bdat')

# df.to_clipboard()
df.to_clipboard()

# df.to_string()
df.to_string()

# df.to_latex()
df.to_latex()

# df.to_xml()
df.to_xml('output.xml')

print("\nSECTION 23: COMPARISON & ALIGNMENT")

# df.compare()
df.compare(df2)

# df.eq()
df.eq(df2)

# df.ne()
df.ne(df2)

# df.lt()
df.lt(df2)

# df.gt()
df.gt(df2)

# df.le()
df.le(df2)

# df.ge()
df.ge(df2)

# pd.eval()
pd.eval('df.A + df.B')

# pd.eval()
pd.eval('2 * df.A + 3')

print("\nSECTION 24: COMBINING (element-wise)")

# df.add()
df.add(df2)

# df.sub()
df.sub(df2)

# df.mul()
df.mul(df2)

# df.div()
df.div(df2)

# df.truediv()
df.truediv(df2)

# df.floordiv()
df.floordiv(df2)

# df.mod()
df.mod(df2)

# df.pow()
df.pow(2)

# df.dot()
df.dot(df2)

# df.radd()
df.radd(df2)

# df.rsub()
df.rsub(df2)

# df.rmul()
df.rmul(df2)

# df.rdiv()
df.rdiv(df2)

# df.rtruediv()
df.rtruediv(df2)

# df.rfloordiv()
df.rfloordiv(df2)

# df.rmod()
df.rmod(df2)

# df.rpow()
df.rpow(2)

print("\nSECTION 25: GENERAL UTILITIES")

# pd.show_versions()
pd.show_versions()

# pd.get_option()
pd.get_option('display.max_rows')

# pd.set_option()
pd.set_option('display.max_columns', 10)

# pd.reset_option()
pd.reset_option('display.max_rows')

# pd.describe_option()
pd.describe_option('display')

# pd.option_context()
with pd.option_context('display.max_rows', 5):
    print(df)

# pd.infer_freq()
pd.infer_freq(df['col'])

# pd.testing.assert_frame_equal()
pd.testing.assert_frame_equal(df, df2)

# pd.testing.assert_series_equal()
pd.testing.assert_series_equal(s, s2)

# pd.testing.assert_index_equal()
pd.testing.assert_index_equal(df.index, df2.index)

# pd.array
pd.array([1, 2, 3], dtype='Int64')

# pd.NA
pd.NA

# pd.NaT
pd.NaT

# pd.notna()
pd.notna(df)

# pd.isna()
pd.isna(df)

# pd.core.nulls.NA
print(pd.NA)
print(pd.NaT)

# pd.factorize()
codes, uniques = pd.factorize(['b', 'b', 'a', 'c', 'a'])

# pd.get_dummies()
pd.get_dummies(df, columns=['col'])

# pd.unique()
pd.unique(df['col'])

# pd.isnull()
pd.isnull(df)

# pd.notnull()
pd.notnull(df)

print("\nSECTION 26: STYLE & DISPLAY")

# df.style
df.style.highlight_max()

# df.to_markdown()
df.to_markdown()

# df.to_records()
df.to_records()

# df.style.set_caption()
df.style.set_caption("Table")

# df.style.background_gradient()
df.style.background_gradient(cmap='Blues')

# df.style.format()
df.style.format('{:.2f}')

print("\nSECTION 27: THIRD-PARTY I/O")

# pd.read_orc()
# pd.read_orc('file.orc') — requires pyarrow

# pd.read_spss()
# pd.read_spss('file.sav') — requires pyreadstat

# pd.io.sql.read_sql_table()
pd.io.sql.read_sql_table('table_name', con=engine)

# pd.io.clipboards.read_clipboard()
# pd.read_clipboard()

print("\nSECTION 28: TIME ZONE")

# df.tz_localize()
df['col'].dt.tz_localize('UTC')

# df.tz_convert()
df['col'].dt.tz_convert('US/Eastern')

print("\nSECTION 29: FREQUENCY CONVERSIONS")

# df.asfreq()
df.asfreq('D')

# df.shift()
df.shift(1, freq='D')

print("\nSECTION 30: OTHER HELPFUL FUNCTIONS")

# df.corr()
df.corr()

# df.cov()
df.cov()

# df.abs()
df.abs()

# df.clip()
df.clip(lower=0)

# df.mask()
df.mask(df > 0, 0)

# df.where()
df.where(df > 0)

# df.squeeze()
df.squeeze()

# df.pipe()
df.pipe(func)

# df.align()
df.align(df2, join='inner', axis=0)

print("\nSECTION 31: ALL COMPLETED.")
