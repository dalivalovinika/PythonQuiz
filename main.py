import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
excel_file = pd.read_csv('survey_results_public.csv')

# გამოიტანთ ცხრილის სასურველ სტრიქონებს და სვეტებს
subset = excel_file.iloc[1:5, 2:4]
# print(subset)


df = pd.DataFrame(excel_file)

# დაუნიშნეთ ინდექსირება ცხრილის კონკრეტული სვეტის მიმართ;
df = df.set_index('ResponseId')
# print(df)


# შექმნით 2 პარამეტრზე დამოკიდებულ ფილტრს. დაბეჭდეთ შესაბამისი ცხრილი.
filtered_df = df[(df['Age'] == '25-34 years old') & (df['YearsCodePro'] == '7')]
# print(filtered_df)

#დაასორტირეთ ცხრილი 2 პარამეტრის გამოყენებით
df = df.sort_values(by=['Age', 'YearsCode'])
# print(df)

#გამოიყენეთ კონკრეტული სვეტის მნიშვნელობისთვის სტატისტიკური ფუნქციები (mean, standard, deviation, median, min, max).
# df_r = pd.to_numeric(df['YearsCodePro'], errors='coerce').mean()
# df_r = pd.to_numeric(df['YearsCodePro'], errors='coerce').std()
# df_r = pd.to_numeric(df['YearsCodePro'], errors='coerce').median()
# df_r = pd.to_numeric(df['YearsCodePro'], errors='coerce').min()
df_r = pd.to_numeric(df['YearsCodePro'], errors='coerce').max()
# print(df_r)

data = df[(df['Age'] == '25-34 years old') & (pd.to_numeric(df['YearsCodePro'], errors='coerce') > 7) & (df['Age'] == '45-54 years old')]
data1 = data.loc[:, ['Age']]
data2 = data.loc[:, ['YearsCodePro']]

plt.bar(data1, data2)
plt.xlabel('age')
plt.ylabel('years')
plt.title('123')

plt.show()