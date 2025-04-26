import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'api_comex', 'src'))

from consulta_comex import consulta_comex 

def etl(ano_inicio, ano_fim):
    df_export = consulta_comex('export', ano_inicio, ano_fim)
    df_import = consulta_comex('import', ano_inicio, ano_fim)
    df = pd.concat([df_import, df_export], ignore_index=True)

    df['DATA'] = pd.to_datetime(df['year'].astype(str) + '-' + df['monthNumber'].astype(str) + '-01')

    df.rename(columns={
        'noMunMinsgUf': 'NO_MUN',
        'country': 'NO_PAIS',
        'chapter': 'NO_SH2_POR',
        'metricFOB': 'VL_FOB',
        'flow': 'CATEGORIA'
    }, inplace=True)

    df.drop(columns=['year', 'monthNumber', 'chapterCode'], inplace=True)
    df['CATEGORIA'] = df['CATEGORIA'].replace({'export': 'EXPORTACAO', 'import': 'IMPORTACAO'})
    df['NO_MUN'] = df['NO_MUN'].str.replace(' - AL', '', regex=False)

    df = df[['DATA', 'NO_MUN', 'NO_PAIS','economicBlock', 'NO_SH2_POR', 'VL_FOB', 'CATEGORIA']]

    # Data ter apenas ANO E MES
    df['DATA'] = df['DATA'].dt.strftime('%Y-%m')

    return df
    # print(df.head())