**Part 1:** Выбор Сценария

Для данной работы выбран сценарий: **Сервис потоковой передачи музыки**. Эта система будет управлять артистами, альбомами, песнями, пользователями и пользовательскими плейлистами.

**Part 2:** Проектирование Базы Данных и Документация

**Идентификация Сущностей и Атрибутов:**

1. **Артисты (Artists) – исполнитель музыки.**

   *Атрибуты:* ID, Имя/Псевдоним, Жанр, Страна, Дата создания аккаунта.

1. **Альбом (Album) - сборник песен.**

   *Атрибуты:*** ID, Название, ID Артиста, Год выпуска, Обложка (URL).

1. **Треки (Tracks) –** единица контекта.

   *Атрибуты:* ID, Название, ID Альбом, Длительность (в секундах), Количество прослушиваний, Является ли синглом.

1. **Пользователь (User)** — слушатель сервиса.

   *Атрибуты:* ID, Имя, Email, Пароль (хэш), Дата регистрации, Тип подписки (бесплатный/премиум).

1. **Плейлист (Playlist)** — пользовательская подборка треков.

   *Атрибуты:* ID, Название, ID Владельца (User), Описание, Дата создания, Приватность (публичный/личный).

**Проектирование Таблиц:**

1. **Table Name: Artists**

**○** **Description:** Хранит информацию о музыкальных исполнителях.

**○** **Attributes:**

- ` `*ID:* INTEGER, PK, NOT NULL, UNIQUE
- *Name:* VARCHAR(100), NOT NULL
- *Genre:* VARCHAR(50)
- *Country:* VARCHAR(50)
- *Created\_At:* TIMESTAMP

○ **Constraints:**

- *PK*\_*Artists:* PRIMARY KEY (id)
- *UQ*\_*ArtistName:* UNIQUE (name)
- *DFT\_Genre:* DEFAULT ‘Pop’
- *DFT\_CreatedAt:* DEFAULT CURRENT\_TIMESTAMP
1. **Table Name: Albums**

**○** **Description:** Хранит альбомы, выпущенные артистами.

○ **Attributes:**

- *ID:* INTEGER, PK, NOT NULL, UNIQUE
- *Title:* VARCHAR(150), NOT NULL
- *ArtistID*: INTEGER, FK (REFERENCES Artists)
- *Release\_Year:* INTEGER
- *Cover\_URL:* TEXT

○ **Constraints:**

- *PK\_Albums:* PRIMARY KEY (id)
- *CHK\_ReleaseYear:* CHECK (release\_year > 1900)
- *FK*\_*AlbumsArtists:* FOREIGN KEY (ArtistID) REFERENCES Artists(ID) ON DELETE CASCADE
1. **Table Name: Tracks**

**○** **Description:** Хранит песни. Связана с альбомом (один ко многим). 

○ **Attributes:**

- *ID:* SERIAL, PK
- *Title:* VARCHAR(150), NOT NULL
- *AlbumID*: INTEGER, FK (REFERENCES Albums)
- *Duration\_Sec:* INTEGER
- *Is\_Single:* BOOLEAN
- *Play\_Count:* INTEGER

○ **Constraints:**

- PK\_Tracks: PRIMARY KEY (ID)
- FK\_TracksAlbums: FOREIGN KEY (AlbumID) REFERENCES Albums(ID) ON DELETE CASCADE
- CHK\_DurationSec: CHECK (duration\_sec > 0)
- DFT\_IsSingle: DEFAULT FALSE
- DFT\_PlayCount: DEFAULT 0
1. **Table Name: Users**

**○** **Description:** Аккаунты слушателей.

○ **Attributes:**

- *ID:* SERIAL, PK
- *Username:* VARCHAR(50), NOT NULL
- *Email:* VARCHAR(100), NOT NULL
- *Password\_Hash:* TEXT, NOT NULL
- *Subscription\_Type:* VARCHAR(20)
- *Registered\_At:* TIMESTAMP

○ **Constraints:**

- PK\_User: PRIMARY KEY (ID)
- UQ\_UserName: UNIQUE (Username)
- UQ\_UserEmail: UNIQUE (Email)
- CHK\_SubscriptionType: CHECK (Subscription\_Type IN ('free', 'premium')), DEFAULT 'free'
- DFT\_RegisteredAt: DEFAULT CURRENT\_TIMESTAMP
1. **Table Name: Playlists**

**○** **Description:** Плейлисты пользователей.

○ **Attributes:** 

- *ID:* SERIAL, PK
- *Name:* VARCHAR(100), NOT NULL
- *Description:* TEXT
- *UserID:* INTEGER, FK (REFERENCES Users)
- *Is\_Public:* BOOLEAN

○ **Constraints:**

- PK\_Playlist: PRIMARY KEY (ID)
- FK\_PlaylistsUser: FOREIGN KEY (UserID) REFERENCES Users(ID) ON DELETE CASCADE
- DFT\_IsPublic: DEFAULT TRUE
1. **Table Name: Playlist\_tracks**

**○** **Description:** Техническая таблица, чтобы связывать плейлисты и треки. Один плейлист содержит много треков, один трек может быть во многих плейлистах.

○ **Attributes:** 

- *PlaylistID:* INTEGER, PK, FK (REFERENCES Playlists)
- *TrackID:* INTEGER, PK, FK (REFERENCES Tracks)
- *Added\_At:* TIMESTAMP

○ **Constraints:**

- PK\_PlaylistTracks: PRIMARY KEY (PlaylistID, TrackID)
- FK\_PlaylistsTracks\_Playlist: FOREIGN KEY (PlaylistID) REFERENCES Playlists(ID) ON DELETE CASCADE
- FK\_PlaylistsTracks\_Track: FOREIGN KEY (TrackID) REFERENCES Tracks(ID) ON DELETE CASCADE
- DFT\_AddedAt: DEFAULT CURRENT\_TIMESTAMP

**Взаимосвязи:**

● **Artists и Albums (Один-ко-Многим):** Один артист может выпустить много альбомов. Каждый альбом принадлежит ровно одному артисту.

○ Albums.ArtistID является внешним ключом, ссылающимся на Artists.ID.

● **Albums и Tracks (Один-ко-Многим):** Один альбом содержит много треков. Один трек принадлежит ровно одному альбому.

○ Tracks.AlbumID является внешним ключом, ссылающимся на Albums.ID.

● **Users и Playlists (Один-ко-Многим):** Один пользователь может создать много плейлистов. Каждый плейлист создан ровно одним пользователем.

○ Playlists.UserID является внешним ключом, ссылающимся на Users.ID.

● **Playlist\_tracks (Многие-ко-многим):** Один плейлист может содержать множество разных треков. Один трек может находиться в множестве разных плейлистов

○ реализована через промежуточную таблицу Playlist\_tracks, где PlaylistID и TrackID — внешние ключи, образующие составной первичный ключ.

