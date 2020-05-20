TYPES = [
  ['ノーマル'],
  ['ほのお'],
  ['みず'],
  ['でんき'],
  ['くさ'],
  ['こおり'],
  ['かくとう'],
  ['どく'],
  ['じめん'],
  ['ひこう'],
  ['エスパー'],
  ['むし'],
  ['いわ'],
  ['ゴースト'],
  ['ドラゴン'],
  ['あく'],
  ['はがね'],
  ['フェアリー']
]

WEAKNESS_LIST = [
  {
    'types': ['ノーマル'],
    'weakness': {
      'single': ['かくとう'],
      'double': []
    },
    'strength': {
      'single': [],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ほのお'],
    'weakness': {
      'single': ['みず', 'じめん', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'くさ', 'こおり', 'むし', 'はがね', 'フェアリー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず'],
    'weakness': {
      'single': ['でんき', 'くさ'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき'],
    'weakness': {
      'single': ['じめん'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'ひこう', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'どく', 'ひこう', 'むし'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり'],
    'weakness': {
      'single': ['ほのお', 'かくとう', 'いわ', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['こおり'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう'],
    'weakness': {
      'single': ['ひこう', 'エスパー', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['むし', 'いわ', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['どく'],
    'weakness': {
      'single': ['じめん', 'エスパー'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'どく', 'むし', 'フェアリー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['じめん'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'いわ'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['ひこう'],
    'weakness': {
      'single': ['でんき', 'こおり', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'むし'],
      'double': [],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['エスパー'],
    'weakness': {
      'single': ['むし', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': ['かくとう', 'エスパー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['むし'],
    'weakness': {
      'single': ['ほのお', 'ひこう', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['いわ'],
    'weakness': {
      'single': ['みず', 'くさ', 'かくとう', 'じめん', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'どく', 'ひこう'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['ゴースト'],
    'weakness': {
      'single': ['エスパー', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'むし'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['ドラゴン'],
    'weakness': {
      'single': ['こおり', 'ドラゴン', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['あく'],
    'weakness': {
      'single': ['かくとう', 'むし', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['はがね'],
    'weakness': {
      'single': ['ほのお', 'かくとう', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'くさ',
        'こおり',
        'ひこう',
        'エスパー',
        'むし',
        'いわ',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': [],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['フェアリー'],
    'weakness': {
      'single': ['どく', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['かくとう', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'ほのお'],
    'weakness': {
      'single': ['みず', 'かくとう', 'じめん', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'くさ', 'こおり', 'むし', 'はがね', 'フェアリー'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'みず'],
    'weakness': {
      'single': ['でんき', 'くさ', 'かくとう'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'はがね'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'でんき'],
    'weakness': {
      'single': ['かくとう', 'じめん'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'ひこう', 'はがね'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'くさ'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'かくとう', 'どく', 'ひこう', 'むし'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'かくとう'],
    'weakness': {
      'single': ['かくとう', 'ひこう', 'エスパー', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['むし', 'いわ', 'あく'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'じめん'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり', 'かくとう'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'いわ'],
      'double': [],
      'noEffect': ['でんき', 'ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'ひこう'],
    'weakness': {
      'single': ['でんき', 'こおり', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'むし'],
      'double': [],
      'noEffect': ['じめん', 'ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'エスパー'],
    'weakness': {
      'single': ['むし', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['エスパー'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'かくとう', 'ドラゴン', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ'],
      'double': [],
      'noEffect': ['ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'あく'],
    'weakness': {
      'single': ['むし', 'フェアリー'],
      'double': ['かくとう']
    },
    'strength': {
      'single': ['あく'],
      'double': [],
      'noEffect': ['エスパー', 'ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ノーマル', 'フェアリー'],
    'weakness': {
      'single': ['どく', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン', 'ゴースト']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'みず'],
    'weakness': {
      'single': ['でんき', 'じめん', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['むし', 'フェアリー'],
      'double': ['ほのお', 'こおり', 'はがね'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'でんき'],
    'weakness': {
      'single': ['みず', 'いわ'],
      'double': ['じめん']
    },
    'strength': {
      'single': [
        'ほのお',
        'でんき',
        'くさ',
        'こおり',
        'ひこう',
        'むし',
        'フェアリー'
      ],
      'double': ['はがね'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'こおり'],
    'weakness': {
      'single': ['みず', 'かくとう', 'じめん'],
      'double': ['いわ']
    },
    'strength': {
      'single': ['くさ', 'むし', 'フェアリー'],
      'double': ['こおり'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'かくとう'],
    'weakness': {
      'single': ['みず', 'じめん', 'ひこう', 'エスパー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'くさ', 'こおり', 'あく', 'はがね'],
      'double': ['むし'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'どく'],
    'weakness': {
      'single': ['みず', 'エスパー', 'いわ'],
      'double': ['じめん']
    },
    'strength': {
      'single': ['ほのお', 'こおり', 'かくとう', 'どく', 'はがね'],
      'double': ['くさ', 'むし', 'フェアリー'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'じめん'],
    'weakness': {
      'single': ['じめん'],
      'double': ['みず']
    },
    'strength': {
      'single': ['ほのお', 'どく', 'むし', 'はがね', 'フェアリー'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'ひこう'],
    'weakness': {
      'single': ['みず', 'でんき'],
      'double': ['いわ']
    },
    'strength': {
      'single': ['ほのお', 'かくとう', 'はがね', 'フェアリー'],
      'double': ['くさ', 'むし'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'エスパー'],
    'weakness': {
      'single': ['みず', 'じめん', 'いわ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': [
        'ほのお',
        'くさ',
        'こおり',
        'かくとう',
        'エスパー',
        'はがね',
        'フェアリー'
      ],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'むし'],
    'weakness': {
      'single': ['みず', 'ひこう'],
      'double': ['いわ']
    },
    'strength': {
      'single': ['こおり', 'かくとう', 'むし', 'はがね', 'フェアリー'],
      'double': ['くさ'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'いわ'],
    'weakness': {
      'single': ['かくとう', 'いわ'],
      'double': ['みず', 'じめん']
    },
    'strength': {
      'single': ['ノーマル', 'こおり', 'どく', 'ひこう', 'むし', 'フェアリー'],
      'double': ['ほのお'],
      'noEffect': ['']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'ゴースト'],
    'weakness': {
      'single': ['みず', 'じめん', 'いわ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'くさ', 'こおり', 'どく', 'はがね', 'フェアリー'],
      'double': ['むし'],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'ドラゴン'],
    'weakness': {
      'single': ['じめん', 'いわ', 'ドラゴン'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'むし', 'はがね'],
      'double': ['ほのお', 'くさ'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'あく'],
    'weakness': {
      'single': ['みず', 'かくとう', 'じめん', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'くさ', 'こおり', 'ゴースト', 'あく', 'はがね'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['ほのお', 'はがね'],
    'weakness': {
      'single': ['みず', 'かくとう'],
      'double': ['じめん']
    },
    'strength': {
      'single': ['ノーマル', 'ひこう', 'エスパー', 'ドラゴン'],
      'double': ['くさ', 'こおり', 'むし', 'はがね', 'フェアリー'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['みず', 'でんき'],
    'weakness': {
      'single': ['くさ', 'じめん'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'ひこう'],
      'double': ['はがね'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'くさ'],
    'weakness': {
      'single': ['どく', 'ひこう', 'むし'],
      'double': []
    },
    'strength': {
      'single': ['じめん', 'はがね'],
      'double': ['みず'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'こおり'],
    'weakness': {
      'single': ['でんき', 'くさ', 'かくとう', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['ほのお'],
      'double': ['こおり'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'かくとう'],
    'weakness': {
      'single': ['でんき', 'くさ', 'ひこう', 'エスパー', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'むし', 'いわ', 'あく', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'どく'],
    'weakness': {
      'single': ['でんき', 'じめん', 'エスパー'],
      'double': []
    },
    'strength': {
      'single': [
        'ほのお',
        'みず',
        'こおり',
        'かくとう',
        'どく',
        'むし',
        'はがね',
        'フェアリー'
      ],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'じめん'],
    'weakness': {
      'single': [],
      'double': ['くさ']
    },
    'strength': {
      'single': ['ほのお', 'どく', 'いわ', 'はがね'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['みず', 'ひこう'],
    'weakness': {
      'single': ['いわ'],
      'double': ['でんき']
    },
    'strength': {
      'single': ['ほのお', 'みず', 'かくとう', 'むし', 'はがね'],
      'double': ['じめん'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'エスパー'],
    'weakness': {
      'single': ['でんき', 'くさ', 'むし', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'かくとう', 'エスパー', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'むし'],
    'weakness': {
      'single': ['でんき', 'ひこう', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'こおり', 'かくとう', 'じめん', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'いわ'],
    'weakness': {
      'single': ['でんき', 'かくとう', 'じめん'],
      'double': ['くさ']
    },
    'strength': {
      'single': ['ノーマル', 'こおり', 'どく', 'ひこう'],
      'double': ['ほのお'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'ゴースト'],
    'weakness': {
      'single': ['でんき', 'くさ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'どく', 'むし', 'はがね'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['みず', 'ドラゴン'],
    'weakness': {
      'single': ['ドラゴン', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['はがね'],
      'double': ['ほのお', 'みず'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'あく'],
    'weakness': {
      'single': ['でんき', 'くさ', 'かくとう', 'むし', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'ゴースト', 'あく', 'はがね'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['みず', 'はがね'],
    'weakness': {
      'single': ['でんき', 'かくとう', 'じめん'],
      'double': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'みず',
        'ひこう',
        'エスパー',
        'むし',
        'いわ',
        'ドラゴン',
        'フェアリー'
      ],
      'double': ['こおり', 'はがね'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['みず', 'フェアリー'],
    'weakness': {
      'single': ['でんき', 'くさ', 'どく'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'こおり', 'かくとう', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'くさ'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'どく', 'むし'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'くさ', 'はがね'],
      'double': ['でんき'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'こおり'],
    'weakness': {
      'single': ['ほのお', 'かくとう', 'じめん', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'こおり', 'ひこう'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'どく'],
    'weakness': {
      'single': ['エスパー'],
      'double': ['じめん']
    },
    'strength': {
      'single': [
        'でんき',
        'くさ',
        'かくとう',
        'どく',
        'ひこう',
        'むし',
        'はがね',
        'フェアリー'
      ],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'じめん'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり', 'じめん'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'ひこう', 'いわ', 'はがね'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'ひこう'],
    'weakness': {
      'single': ['こおり', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'ひこう', 'むし', 'はがね'],
      'double': [],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'エスパー'],
    'weakness': {
      'single': ['じめん', 'むし', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'かくとう', 'ひこう', 'エスパー', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'むし'],
    'weakness': {
      'single': ['ほのお', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'くさ', 'かくとう', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'いわ'],
    'weakness': {
      'single': ['みず', 'くさ', 'かくとう'],
      'double': ['じめん']
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'でんき', 'どく'],
      'double': ['ひこう'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'ゴースト'],
    'weakness': {
      'single': ['じめん', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'どく', 'ひこう', 'むし', 'はがね'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'じめん', 'ドラゴン', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'くさ', 'ひこう', 'はがね'],
      'double': ['でんき'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['でんき', 'あく'],
    'weakness': {
      'single': ['かくとう', 'じめん', 'むし', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'ひこう', 'ゴースト', 'あく', 'はがね'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'かくとう'],
      'double': ['じめん']
    },
    'strength': {
      'single': [
        'ノーマル',
        'でんき',
        'くさ',
        'こおり',
        'エスパー',
        'むし',
        'いわ',
        'ドラゴン',
        'フェアリー'
      ],
      'double': ['ひこう', 'はがね'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['でんき', 'フェアリー'],
    'weakness': {
      'single': ['どく', 'じめん'],
      'double': []
    },
    'strength': {
      'single': ['でんき', 'かくとう', 'ひこう', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'こおり'],
    'weakness': {
      'single': ['かくとう', 'どく', 'ひこう', 'むし', 'いわ', 'はがね'],
      'double': ['ほのお']
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'かくとう'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'どく', 'エスパー', 'フェアリー'],
      'double': ['ひこう']
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん', 'いわ', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'どく'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'ひこう', 'エスパー'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'でんき', 'かくとう', 'フェアリー'],
      'double': ['くさ'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'じめん'],
    'weakness': {
      'single': ['ほのお', 'ひこう', 'むし'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['じめん', 'いわ'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'ひこう'],
    'weakness': {
      'single': ['ほのお', 'どく', 'ひこう', 'いわ'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['みず', 'かくとう'],
      'double': ['くさ'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'エスパー'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'どく', 'ひこう', 'ゴースト', 'あく'],
      'double': ['むし']
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'かくとう', 'じめん', 'エスパー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'むし'],
    'weakness': {
      'single': ['こおり', 'どく', 'むし', 'いわ'],
      'double': ['ほのお', 'ひこう']
    },
    'strength': {
      'single': ['みず', 'でんき', 'かくとう'],
      'double': ['くさ', 'じめん'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'いわ'],
    'weakness': {
      'single': ['こおり', 'かくとう', 'むし', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'でんき'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'ゴースト'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'ひこう', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'ドラゴン'],
    'weakness': {
      'single': ['どく', 'ひこう', 'むし', 'ドラゴン', 'フェアリー'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['じめん'],
      'double': ['みず', 'でんき', 'くさ'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['くさ', 'あく'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'かくとう', 'どく', 'ひこう', 'フェアリー'],
      'double': ['むし']
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'じめん', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'はがね'],
    'weakness': {
      'single': ['かくとう'],
      'double': ['ほのお']
    },
    'strength': {
      'single': [
        'ノーマル',
        'みず',
        'でんき',
        'エスパー',
        'いわ',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['くさ'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['くさ', 'フェアリー'],
    'weakness': {
      'single': ['ほのお', 'こおり', 'ひこう', 'はがね'],
      'double': ['どく']
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ', 'かくとう', 'じめん', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'かくとう'],
    'weakness': {
      'single': [
        'ほのお',
        'かくとう',
        'ひこう',
        'エスパー',
        'はがね',
        'フェアリー'
      ],
      'double': []
    },
    'strength': {
      'single': ['こおり', 'むし', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり', 'じめん'],
    'weakness': {
      'single': ['ほのお', 'みず', 'くさ', 'かくとう', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['どく'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'ひこう'],
    'weakness': {
      'single': ['ほのお', 'でんき', 'はがね'],
      'double': ['いわ']
    },
    'strength': {
      'single': ['くさ', 'むし'],
      'double': [],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'エスパー'],
    'weakness': {
      'single': ['ほのお', 'むし', 'いわ', 'ゴースト', 'あく', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['こおり', 'エスパー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり', 'むし'],
    'weakness': {
      'single': ['ひこう', 'はがね'],
      'double': ['ほのお', 'いわ']
    },
    'strength': {
      'single': ['くさ', 'こおり', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり', 'いわ'],
    'weakness': {
      'single': ['みず', 'くさ', 'じめん', 'いわ'],
      'double': ['かくとう', 'はがね']
    },
    'strength': {
      'single': ['ノーマル', 'こおり', 'どく', 'ひこう'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり', 'ゴースト'],
    'weakness': {
      'single': ['ほのお', 'いわ', 'ゴースト', 'あく', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['こおり', 'どく', 'むし'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'ドラゴン'],
    'weakness': {
      'single': ['かくとう', 'いわ', 'ドラゴン', 'はがね', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['みず', 'でんき', 'くさ'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['こおり', 'あく'],
    'weakness': {
      'single': ['ほのお', 'むし', 'いわ', 'はがね', 'フェアリー'],
      'double': ['かくとう']
    },
    'strength': {
      'single': ['こおり', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'はがね'],
    'weakness': {
      'single': ['じめん'],
      'double': ['ほのお', 'かくとう']
    },
    'strength': {
      'single': [
        'ノーマル',
        'くさ',
        'ひこう',
        'エスパー',
        'むし',
        'ドラゴン',
        'フェアリー'
      ],
      'double': ['こおり'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['こおり', 'フェアリー'],
    'weakness': {
      'single': ['ほのお', 'どく', 'いわ'],
      'double': ['はがね']
    },
    'strength': {
      'single': ['こおり', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'どく'],
    'weakness': {
      'single': ['じめん', 'ひこう'],
      'double': ['エスパー']
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'どく', 'いわ', 'あく'],
      'double': ['むし'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'ひこう'],
    'weakness': {
      'single': ['でんき', 'こおり', 'ひこう', 'エスパー', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'あく'],
      'double': ['むし'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'エスパー'],
    'weakness': {
      'single': ['ひこう', 'ゴースト', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['かくとう', 'いわ'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'むし'],
    'weakness': {
      'single': ['ほのお', 'エスパー', 'フェアリー'],
      'double': ['ひこう']
    },
    'strength': {
      'single': ['くさ', 'かくとう', 'じめん', 'むし', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'いわ'],
    'weakness': {
      'single': [
        'みず',
        'くさ',
        'かくとう',
        'じめん',
        'エスパー',
        'はがね',
        'フェアリー'
      ],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'どく', 'むし', 'いわ', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'ゴースト'],
    'weakness': {
      'single': ['ひこう', 'エスパー', 'ゴースト', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'いわ'],
      'double': ['むし'],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'ひこう', 'エスパー', 'ドラゴン'],
      'double': ['フェアリー']
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ', 'むし', 'いわ', 'あく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'あく'],
    'weakness': {
      'single': ['かくとう', 'ひこう'],
      'double': ['フェアリー']
    },
    'strength': {
      'single': ['いわ', 'ゴースト'],
      'double': ['あく'],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['かくとう', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'かくとう', 'じめん'],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'くさ', 'こおり', 'ドラゴン', 'あく', 'はがね'],
      'double': ['むし', 'いわ'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['どく', 'じめん'],
    'weakness': {
      'single': ['みず', 'こおり', 'じめん', 'エスパー'],
      'double': []
    },
    'strength': {
      'single': ['かくとう', 'むし', 'いわ', 'フェアリー'],
      'double': ['どく'],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['どく', 'ひこう'],
    'weakness': {
      'single': ['でんき', 'こおり', 'エスパー', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'フェアリー'],
      'double': ['くさ', 'かくとう', 'むし'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['どく', 'むし'],
    'weakness': {
      'single': ['ほのお', 'ひこう', 'エスパー', 'いわ'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'むし', 'フェアリー'],
      'double': ['くさ', 'かくとう'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['どく', 'いわ'],
    'weakness': {
      'single': ['みず', 'エスパー', 'はがね'],
      'double': ['じめん']
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'ひこう', 'むし', 'フェアリー'],
      'double': ['どく'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['どく', 'ゴースト'],
    'weakness': {
      'single': ['じめん', 'エスパー', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'フェアリー'],
      'double': ['どく', 'むし'],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['どく', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'じめん', 'エスパー', 'ドラゴン'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'かくとう', 'どく', 'むし'],
      'double': ['くさ'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['どく', 'あく'],
    'weakness': {
      'single': ['じめん'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'どく', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['どく', 'フェアリー'],
    'weakness': {
      'single': ['じめん', 'エスパー', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'あく', 'フェアリー'],
      'double': ['かくとう', 'むし'],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'ひこう'],
    'weakness': {
      'single': ['みず'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['かくとう', 'どく', 'むし'],
      'double': [],
      'noEffect': ['でんき', 'じめん']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'エスパー'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり', 'むし', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['かくとう', 'どく', 'エスパー', 'いわ'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'むし'],
    'weakness': {
      'single': ['ほのお', 'みず', 'こおり', 'ひこう'],
      'double': []
    },
    'strength': {
      'single': ['かくとう', 'どく', 'じめん'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'いわ'],
    'weakness': {
      'single': ['こおり', 'かくとう', 'じめん', 'はがね'],
      'double': ['みず', 'くさ']
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'ひこう', 'いわ'],
      'double': ['どく'],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'ゴースト'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['むし', 'いわ'],
      'double': ['どく'],
      'noEffect': ['ノーマル', 'でんき', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'ドラゴン'],
    'weakness': {
      'single': ['ドラゴン', 'フェアリー'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['ほのお', 'どく', 'いわ'],
      'double': [],
      'noEffect': ['でんき']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'あく'],
    'weakness': {
      'single': ['みず', 'くさ', 'こおり', 'かくとう', 'むし', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['どく', 'いわ', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['でんき', 'エスパー']
    },
    'skills': []
  },
  {
    'types': ['じめん', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'みず', 'かくとう', 'じめん'],
      'double': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'ひこう',
        'エスパー',
        'むし',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['いわ'],
      'noEffect': ['でんき', 'どく']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'エスパー'],
    'weakness': {
      'single': ['でんき', 'こおり', 'いわ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'エスパー'],
      'double': ['かくとう'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'むし'],
    'weakness': {
      'single': ['ほのお', 'でんき', 'こおり', 'ひこう'],
      'double': ['いわ']
    },
    'strength': {
      'single': ['むし'],
      'double': ['くさ', 'かくとう'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'いわ'],
    'weakness': {
      'single': ['みず', 'でんき', 'こおり', 'いわ', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'どく', 'ひこう', 'むし'],
      'double': [],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'ゴースト'],
    'weakness': {
      'single': ['でんき', 'こおり', 'いわ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'どく'],
      'double': ['むし'],
      'noEffect': ['ノーマル', 'かくとう', 'じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'ドラゴン'],
    'weakness': {
      'single': ['いわ', 'ドラゴン', 'フェアリー'],
      'double': ['こおり']
    },
    'strength': {
      'single': ['ほのお', 'みず', 'かくとう', 'むし'],
      'double': ['くさ'],
      'noEffect': ['じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'あく'],
    'weakness': {
      'single': ['でんき', 'こおり', 'いわ', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['じめん', 'エスパー']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'でんき'],
      'double': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'ひこう',
        'エスパー',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['くさ', 'むし'],
      'noEffect': ['どく', 'じめん']
    },
    'skills': []
  },
  {
    'types': ['ひこう', 'フェアリー'],
    'weakness': {
      'single': ['でんき', 'こおり', 'どく', 'いわ', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'あく'],
      'double': ['かくとう', 'むし'],
      'noEffect': ['じめん', 'ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'むし'],
    'weakness': {
      'single': [
        'ほのお',
        'じめん',
        'ひこう',
        'むし',
        'いわ',
        'ゴースト',
        'あく'
      ],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': ['くさ', 'エスパー'],
      'double': ['かくとう'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'いわ'],
    'weakness': {
      'single': ['みず', 'くさ', 'じめん', 'むし', 'ゴースト', 'あく', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'どく', 'ひこう', 'エスパー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'ゴースト'],
    'weakness': {
      'single': [],
      'double': ['ゴースト', 'あく'],
      'noEffect': []
    },
    'strength': {
      'single': ['どく', 'エスパー'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'むし', 'ゴースト', 'ドラゴン', 'あく', 'フェアリー'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ', 'かくとう', 'エスパー'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'あく'],
    'weakness': {
      'single': ['フェアリー'],
      'double': ['むし'],
      'noEffect': []
    },
    'strength': {
      'single': [],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'じめん', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'くさ',
        'こおり',
        'ひこう',
        'いわ',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['エスパー'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['エスパー', 'フェアリー'],
    'weakness': {
      'single': ['どく', 'ゴースト', 'はがね'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': ['エスパー'],
      'double': ['かくとう'],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['むし', 'いわ'],
    'weakness': {
      'single': ['みず', 'いわ', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'どく'],
      'double': [],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['むし', 'ゴースト'],
    'weakness': {
      'single': ['ほのお', 'ひこう', 'いわ', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'どく', 'じめん', 'むし'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['むし', 'はがね'],
    'weakness': {
      'single': [],
      'double': ['ほのお']
    },
    'strength': {
      'single': [
        'ノーマル',
        'こおり',
        'エスパー',
        'むし',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['くさ'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['むし', 'フェアリー'],
    'weakness': {
      'single': ['ほのお', 'どく', 'ひこう', 'いわ', 'はがね'],
      'double': []
    },
    'strength': {
      'single': ['くさ', 'じめん', 'むし', 'あく'],
      'double': ['かくとう'],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['いわ', 'ドラゴン'],
    'weakness': {
      'single': [
        'こおり',
        'かくとう',
        'じめん',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': []
    },
    'strength': {
      'single': ['ノーマル', 'でんき', 'どく', 'ひこう'],
      'double': ['ほのお'],
      'noEffect': []
    },
    'skills': []
  },
  {
    'types': ['いわ', 'あく'],
    'weakness': {
      'single': ['みず', 'くさ', 'じめん', 'むし', 'はがね', 'フェアリー'],
      'double': ['かくとう']
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'どく', 'ひこう', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['いわ', 'はがね'],
    'weakness': {
      'single': ['みず'],
      'double': ['かくとう', 'じめん']
    },
    'strength': {
      'single': ['こおり', 'エスパー', 'むし', 'いわ', 'ドラゴン', 'フェアリー'],
      'double': ['ノーマル', 'ひこう'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['いわ', 'フェアリー'],
    'weakness': {
      'single': ['みず', 'くさ', 'じめん'],
      'double': ['はがね']
    },
    'strength': {
      'single': ['ノーマル', 'ほのお', 'ひこう', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['ゴースト', 'ドラゴン'],
    'weakness': {
      'single': ['こおり', 'ゴースト', 'ドラゴン', 'あく', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ', 'どく', 'むし'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう']
    },
    'skills': []
  },
  {
    'types': ['ゴースト', 'あく'],
    'weakness': {
      'single': ['フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['どく'],
      'double': [],
      'noEffect': ['ノーマル', 'かくとう', 'エスパー']
    },
    'skills': []
  },
  {
    'types': ['ゴースト', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'じめん', 'ゴースト', 'あく'],
      'double': []
    },
    'strength': {
      'single': [
        'くさ',
        'こおり',
        'ひこう',
        'エスパー',
        'いわ',
        'ドラゴン',
        'はがね',
        'フェアリー'
      ],
      'double': ['むし'],
      'noEffect': ['ノーマル', 'かくとう', 'どく']
    },
    'skills': []
  },
  {
    'types': ['ゴースト', 'フェアリー'],
    'weakness': {
      'single': ['ゴースト', 'はがね'],
      'double': []
    },
    'strength': {
      'single': [],
      'double': ['むし'],
      'noEffect': ['ノーマル', 'かくとう', 'ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['ドラゴン', 'あく'],
    'weakness': {
      'single': ['こおり', 'かくとう', 'むし', 'ドラゴン'],
      'double': ['フェアリー']
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ', 'ゴースト', 'あく'],
      'double': [],
      'noEffect': ['エスパー']
    },
    'skills': []
  },
  {
    'types': ['ドラゴン', 'はがね'],
    'weakness': {
      'single': ['かくとう', 'じめん'],
      'double': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'みず',
        'でんき',
        'ひこう',
        'エスパー',
        'むし',
        'いわ',
        'はがね'
      ],
      'double': ['くさ'],
      'noEffect': ['どく']
    },
    'skills': []
  },
  {
    'types': ['ドラゴン', 'フェアリー'],
    'weakness': {
      'single': ['こおり', 'どく', 'はがね', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ほのお', 'みず', 'でんき', 'くさ', 'かくとう', 'むし', 'あく'],
      'double': [],
      'noEffect': ['ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['あく', 'はがね'],
    'weakness': {
      'single': ['ほのお', 'じめん'],
      'double': ['かくとう']
    },
    'strength': {
      'single': [
        'ノーマル',
        'くさ',
        'こおり',
        'ひこう',
        'いわ',
        'ゴースト',
        'ドラゴン',
        'あく',
        'はがね'
      ],
      'double': [],
      'noEffect': ['どく', 'エスパー']
    },
    'skills': []
  },
  {
    'types': ['あく', 'フェアリー'],
    'weakness': {
      'single': ['どく', 'はがね', 'フェアリー'],
      'double': []
    },
    'strength': {
      'single': ['ゴースト'],
      'double': ['あく'],
      'noEffect': ['エスパー', 'ドラゴン']
    },
    'skills': []
  },
  {
    'types': ['はがね', 'フェアリー'],
    'weakness': {
      'single': ['ほのお', 'じめん'],
      'double': [],
      'noEffect': []
    },
    'strength': {
      'single': [
        'ノーマル',
        'くさ',
        'こおり',
        'ひこう',
        'エスパー',
        'いわ',
        'あく',
        'フェアリー'
      ],
      'double': ['むし'],
      'noEffect': ['どく', 'ドラゴン']
    },
    'skills': []
  }
]


POKEMON_NOT_FOUND_MESSAGE = 'ポケモンの名前を正しく指定して下さい。'


NORMAL_SKILLS = [
{
    "name": "とっしん",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "プレゼント",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "12",
    "rigidity": "3"
  },
  {
    "name": "あくび",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "0",
    "ept": "12",
    "rigidity": "4"
  },
  {
    "name": "めざめるパワー",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "へんしん",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "0",
    "ept": "0",
    "rigidity": "3"
  },
  {
    "name": "いあいぎり",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "2",
    "rigidity": "1"
  },
  {
    "name": "ひっかく",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "2",
    "rigidity": "1"
  },
  {
    "name": "はたく",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "4",
    "rigidity": "2"
  },
  {
    "name": "でんこうせっか",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "たいあたり",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "2",
    "rigidity": "1"
  },
  {
    "name": "ロックオン",
    "type": "ノーマル",
    "category": "ノーマル",
    "dpt": "1",
    "ept": "5",
    "rigidity": "1"
  },
  {
    "name": "むしのていこう",
    "type": "むし",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "まとわりつく",
    "type": "むし",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "11",
    "rigidity": "3"
  },
  {
    "name": "れんぞくぎり",
    "type": "むし",
    "category": "ノーマル",
    "dpt": "2",
    "ept": "4",
    "rigidity": "1"
  },
  {
    "name": "むしくい",
    "type": "むし",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "3",
    "rigidity": "1"
  },
  {
    "name": "たきのぼり",
    "type": "みず",
    "category": "ノーマル",
    "dpt": "12",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "みずでっぽう",
    "type": "みず",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "3",
    "rigidity": "1"
  },
  {
    "name": "はねる",
    "type": "みず",
    "category": "ノーマル",
    "dpt": "0",
    "ept": "12",
    "rigidity": "4"
  },
  {
    "name": "あわ",
    "type": "みず",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "11",
    "rigidity": "3"
  },
  {
    "name": "タネマシンガン",
    "type": "くさ",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "13",
    "rigidity": "3"
  },
  {
    "name": "はっぱカッター",
    "type": "くさ",
    "category": "ノーマル",
    "dpt": "11",
    "ept": "4",
    "rigidity": "2"
  },
  {
    "name": "つるのムチ",
    "type": "くさ",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "8",
    "rigidity": "2"
  },
  {
    "name": "こなゆき",
    "type": "こおり",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "8",
    "rigidity": "2"
  },
  {
    "name": "こおりのつぶて",
    "type": "こおり",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "10",
    "rigidity": "3"
  },
  {
    "name": "こおりのいぶき",
    "type": "こおり",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "こおりのキバ",
    "type": "こおり",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "カウンター",
    "type": "かくとう",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "けたぐり",
    "type": "かくとう",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "からてチョップ",
    "type": "かくとう",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "いわくだき",
    "type": "かくとう",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "7",
    "rigidity": "3"
  },
  {
    "name": "マッドショット",
    "type": "じめん",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "9",
    "rigidity": "2"
  },
  {
    "name": "どろかけ",
    "type": "じめん",
    "category": "ノーマル",
    "dpt": "11",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "いわおとし",
    "type": "いわ",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "うちおとす",
    "type": "いわ",
    "category": "ノーマル",
    "dpt": "12",
    "ept": "8",
    "rigidity": "3"
  },
  {
    "name": "ほのおのうず",
    "type": "ほのお",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "10",
    "rigidity": "3"
  },
  {
    "name": "ほのおのキバ",
    "type": "ほのお",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "ひのこ",
    "type": "ほのお",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "6",
    "rigidity": "2"
  },
  {
    "name": "エアスラッシュ",
    "type": "ひこう",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "9",
    "rigidity": "3"
  },
  {
    "name": "つばさでうつ",
    "type": "ひこう",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "つつく",
    "type": "ひこう",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "アイアンテール",
    "type": "はがね",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "6",
    "rigidity": "3"
  },
  {
    "name": "メタルクロー",
    "type": "はがね",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "6",
    "rigidity": "2"
  },
  {
    "name": "バレットパンチ",
    "type": "はがね",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "はがねのつばさ",
    "type": "はがね",
    "category": "ノーマル",
    "dpt": "7",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "たたりめ",
    "type": "ゴースト",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "11",
    "rigidity": "3"
  },
  {
    "name": "おどろかす",
    "type": "ゴースト",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "9",
    "rigidity": "3"
  },
  {
    "name": "シャドークロー",
    "type": "ゴースト",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "8",
    "rigidity": "2"
  },
  {
    "name": "したでなめる",
    "type": "ゴースト",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "3",
    "rigidity": "1"
  },
  {
    "name": "あまえる",
    "type": "フェアリー",
    "category": "ノーマル",
    "dpt": "16",
    "ept": "6",
    "rigidity": "3"
  },
  {
    "name": "じんつうりき",
    "type": "エスパー",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "10",
    "rigidity": "3"
  },
  {
    "name": "ねんりき",
    "type": "エスパー",
    "category": "ノーマル",
    "dpt": "16",
    "ept": "12",
    "rigidity": "4"
  },
  {
    "name": "しねんのずつき",
    "type": "エスパー",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "6",
    "rigidity": "3"
  },
  {
    "name": "サイコカッター",
    "type": "エスパー",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "9",
    "rigidity": "2"
  },
  {
    "name": "ドラゴンテール",
    "type": "ドラゴン",
    "category": "ノーマル",
    "dpt": "9",
    "ept": "10",
    "rigidity": "3"
  },
  {
    "name": "りゅうのいぶき",
    "type": "ドラゴン",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "3",
    "rigidity": "1"
  },
  {
    "name": "ようかいえき",
    "type": "どく",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "どくばり",
    "type": "どく",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "6",
    "rigidity": "2"
  },
  {
    "name": "どくづき",
    "type": "どく",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "ボルトチェンジ",
    "type": "でんき",
    "category": "ノーマル",
    "dpt": "12",
    "ept": "16",
    "rigidity": "4"
  },
  {
    "name": "チャージビーム",
    "type": "でんき",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "11",
    "rigidity": "3"
  },
  {
    "name": "でんきショック",
    "type": "でんき",
    "category": "ノーマル",
    "dpt": "3",
    "ept": "9",
    "rigidity": "2"
  },
  {
    "name": "スパーク",
    "type": "でんき",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "8",
    "rigidity": "2"
  },
  {
    "name": "かみなりのキバ",
    "type": "でんき",
    "category": "ノーマル",
    "dpt": "8",
    "ept": "5",
    "rigidity": "2"
  },
  {
    "name": "バークアウト",
    "type": "あく",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "13",
    "rigidity": "3"
  },
  {
    "name": "ふいうち",
    "type": "あく",
    "category": "ノーマル",
    "dpt": "5",
    "ept": "7",
    "rigidity": "2"
  },
  {
    "name": "だましうち",
    "type": "あく",
    "category": "ノーマル",
    "dpt": "6",
    "ept": "6",
    "rigidity": "2"
  },
  {
    "name": "かみつく",
    "type": "あく",
    "category": "ノーマル",
    "dpt": "4",
    "ept": "2",
    "rigidity": "1"
  }
]


SPECIAL_SKILLS = [
{
    "name": "わるあがき",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "35",
    "energy": "100",
    "effect": "-"
  },
  {
    "name": "まきつく",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "ふみつけ",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ひっさつまえば",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "はさむ",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "はかいこうせん",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "のしかかり",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "つのでつく",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "スピードスター",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ギガインパクト",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "やつあたり",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "10",
    "energy": "70",
    "effect": "-"
  },
  {
    "name": "おんがえし",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "70",
    "effect": "-"
  },
  {
    "name": "ロケットずつき",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "75",
    "effect": "自:防↑100%"
  },
  {
    "name": "ウェザーボール",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "とっておき",
    "type": "ノーマル",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ぎんいろのかぜ",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "45",
    "effect": "自:攻防↑↑10%"
  },
  {
    "name": "メガホーン",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "むしのさざめき",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "シザークロス",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "シグナルビーム",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "75",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "とどめばり",
    "type": "むし",
    "category": "スペシャル",
    "dpe": "20",
    "energy": "35",
    "effect": "自:攻↑100%"
  },
  {
    "name": "なみのり",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "65",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ねっとう",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "みずのはどう",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "バブルこうせん",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "25",
    "energy": "40",
    "effect": "相:攻↓100%"
  },
  {
    "name": "ハイドロポンプ",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "75",
    "effect": "-"
  },
  {
    "name": "しおみず",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "アクアテール",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "アクアジェット",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "オクタンほう",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "50",
    "effect": "相:攻↓↓50%"
  },
  {
    "name": "クラブハンマー",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "75",
    "energy": "50",
    "effect": "自:攻↑↑12.5%"
  },
  {
    "name": "だくりゅう",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "35",
    "energy": "35",
    "effect": "相:攻↓30%"
  },
  {
    "name": "ウェザーボール(みず)",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "ハイドロカノン",
    "type": "みず",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ハードプラント",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "エナジーボール",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "相:防↓10%"
  },
  {
    "name": "くさむすび",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "リーフブレード",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "はなふぶき",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "パワーウィップ",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "タネばくだん",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ソーラービーム",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "グラスミキサー",
    "type": "くさ",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "40",
    "effect": "相:攻↓↓50%"
  },
  {
    "name": "ゆきなだれ",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "オーロラビーム",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "れいとうビーム",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "れいとうパンチ",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ふぶき",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "75",
    "effect": "-"
  },
  {
    "name": "こごえるかぜ",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "45",
    "effect": "相:攻↓100%"
  },
  {
    "name": "ウェザーボール(こおり)",
    "type": "こおり",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "きあいだま",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "75",
    "effect": "-"
  },
  {
    "name": "ばくれつパンチ",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "インファイト",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "45",
    "effect": "自:防↓↓100%"
  },
  {
    "name": "ローキック",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "じごくぐるま",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "クロスチョップ",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "かわらわり",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "フライングプレス",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "せいなるつるぎ",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "ばかぢから",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "85",
    "energy": "40",
    "effect": "自:攻防↓100%"
  },
  {
    "name": "はどうだん",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "グロウパンチ",
    "type": "かくとう",
    "category": "スペシャル",
    "dpe": "20",
    "energy": "35",
    "effect": "自:攻↑100%"
  },
  {
    "name": "すなじごく",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "25",
    "energy": "40",
    "effect": "相:防↓100%"
  },
  {
    "name": "ホネこんぼう",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "じしん",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "120",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "ドリルライナー",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "どろばくだん",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "じならし",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "あなをほる",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "だいちのちから",
    "type": "じめん",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "相:防↓10%"
  },
  {
    "name": "ロックブラスト",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ストーンエッジ",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "パワージェム",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "げんしのちから",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "45",
    "effect": "自:攻防↑↑10%"
  },
  {
    "name": "がんせきふうじ",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "いわなだれ",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "がんせきほう",
    "type": "いわ",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "ブラストバーン",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "オーバーヒート",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "55",
    "effect": "自:攻↓↓100%"
  },
  {
    "name": "ほのおのパンチ",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "だいもんじ",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "140",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "はじけるほのお",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ニトロチャージ",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "かえんほうしゃ",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "かえんぐるま",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ねっぷう",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "95",
    "energy": "75",
    "effect": "-"
  },
  {
    "name": "ブレイズキック",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ウェザーボール(ほのお)",
    "type": "ほのお",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "ブレイブバード",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ゴッドバード",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "ぼうふう",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "ドリルくちばし",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "つばめがえし",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "エアカッター",
    "type": "ひこう",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "はめつのねがい",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "75",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ヘビーボンバー",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "ジャイロボール",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "アイアンヘッド",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "ラスターカノン",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "マグネットボム",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "ミラーショット",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "35",
    "energy": "35",
    "effect": "相:攻↓30%"
  },
  {
    "name": "コメットパンチ",
    "type": "はがね",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "かげうち",
    "type": "ゴースト",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "シャドーパンチ",
    "type": "ゴースト",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "ナイトヘッド",
    "type": "ゴースト",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "シャドーボール",
    "type": "ゴースト",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "あやしいかぜ",
    "type": "ゴースト",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "45",
    "effect": "自:攻防↑↑10%"
  },
  {
    "name": "ドレインキッス",
    "type": "フェアリー",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "ムーンフォース",
    "type": "フェアリー",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "60",
    "effect": "相:攻↓30%"
  },
  {
    "name": "マジカルシャイン",
    "type": "フェアリー",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "70",
    "effect": "-"
  },
  {
    "name": "チャームボイス",
    "type": "フェアリー",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "じゃれつく",
    "type": "フェアリー",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "サイコブースト",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "35",
    "effect": "自:攻↓↓100%"
  },
  {
    "name": "ミラーコート",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "60",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "みらいよち",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "120",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "サイコショック",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "サイコキネシス",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "相:防↓10%"
  },
  {
    "name": "サイケこうせん",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "サイコブレイク",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "シンクロノイズ",
    "type": "エスパー",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "りゅうせいぐん",
    "type": "ドラゴン",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "65",
    "effect": "自:攻↓↓100%"
  },
  {
    "name": "げきりん",
    "type": "ドラゴン",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "ドラゴンクロー",
    "type": "ドラゴン",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "りゅうのはどう",
    "type": "ドラゴン",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "たつまき",
    "type": "ドラゴン",
    "category": "スペシャル",
    "dpe": "45",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "ヘドロばくだん",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "50",
    "effect": "-"
  },
  {
    "name": "ヘドロこうげき",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "ヘドロウェーブ",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "110",
    "energy": "65",
    "effect": "-"
  },
  {
    "name": "どくどくのキバ",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "ダストシュート",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "130",
    "energy": "75",
    "effect": "-"
  },
  {
    "name": "クロスポイズン",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "40",
    "energy": "35",
    "effect": "-"
  },
  {
    "name": "アシッドボム",
    "type": "どく",
    "category": "スペシャル",
    "dpe": "20",
    "energy": "50",
    "effect": "相:防↓↓100%"
  },
  {
    "name": "でんじほう",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "150",
    "energy": "80",
    "effect": "-"
  },
  {
    "name": "ワイルドボルト",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "45",
    "effect": "自:防↓↓100%"
  },
  {
    "name": "かみなりパンチ",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "55",
    "energy": "40",
    "effect": "-"
  },
  {
    "name": "かみなり",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "100",
    "energy": "60",
    "effect": "-"
  },
  {
    "name": "ほうでん",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "65",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "１０まんボルト",
    "type": "でんき",
    "category": "スペシャル",
    "dpe": "90",
    "energy": "55",
    "effect": "-"
  },
  {
    "name": "イカサマ",
    "type": "あく",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "かみくだく",
    "type": "あく",
    "category": "スペシャル",
    "dpe": "70",
    "energy": "45",
    "effect": "-"
  },
  {
    "name": "つじぎり",
    "type": "あく",
    "category": "スペシャル",
    "dpe": "50",
    "energy": "35",
    "effect": "自:攻↑↑12.5%"
  },
  {
    "name": "あくのはどう",
    "type": "あく",
    "category": "スペシャル",
    "dpe": "80",
    "energy": "50",
    "effect": "-"
  }
]