**Part 1:** Выбор Сценария

Для данной работы выбран сценарий: **Сервис потоковой передачи музыки**. Эта система будет управлять артистами, альбомами, песнями, пользователями и пользовательскими плейлистами.

**Part 2:** Проектирование Базы Данных и Документация

**Идентификация Сущностей и Атрибутов:**

1. **Артисты (Artists) – исполнитель музыки.**

   *Атрибуты:* ID, Имя/Псевдоним, Жанр, Страна, Дата создания аккаунта.

1. **Альбом (Album) - сборник песен.**

   *Атрибуты:*** ID, Название, Год выпуска, Обложка (URL).

1. **Треки (Tracks) –** единица контекта.

   *Атрибуты:* ID, Название, ID Альбом, Длительность (в секундах), Количество прослушиваний, Является ли синглом.

1. **Пользователь (User)** — слушатель сервиса.

   *Атрибуты:* ID, Имя, Email, Пароль (хэш), Дата регистрации, Тип подписки (бесплатный/премиум).

1. **Плейлист (Playlist)** — пользовательская подборка треков.

   *Атрибуты:* ID, Название, ID Владельца (User), Описание, Дата создания, Приватность (публичный/личный).

**Проектирование Таблиц:**

1. **Table Name: Genres**

**○** **Description:** Хранит информацию о разных жанрах музыки.

**○** **Attributes:**

- ` `*ID:* SERIAL, PK
- *Name:* VARCHAR(50), NOT NULL, UNIQUE
- *Description:* TEXT

○ **Constraints:**

- *PK*\_*Genres:* PRIMARY KEY (ID)
- *UQ*\_*GenreName:* UNIQUE (Name)
1. **Table Name: Artists**

**○** **Description:** Хранит информацию о музыкальных исполнителях.

**○** **Attributes:**

- ` `*ID:* INTEGER, PK
- *Name:* VARCHAR(100), NOT NULL
- *Country:* VARCHAR(50)
- *Created\_At:* TIMESTAMP

○ **Constraints:**

- *PK*\_*Artists:* PRIMARY KEY (ID)
- *UQ*\_*ArtistName:* UNIQUE (Name)
- *DFT\_CreatedAt:* DEFAULT CURRENT\_TIMESTAMP
1. **Table Name: Artists\_Genres**

**○** **Description:** Связующая таблица для отношения "многие-ко-многим" между артистами и жанрами.

**○** **Attributes:**

- ` `*ArtistID:* INTEGER, PK, FK (REFERENCES Artists)
- *GenreID:* INTEGER, PK, FK (REFERENCES Genres)* 

○ **Constraints:**

- *PK*\_*ArtistGenres:* PRIMARY KEY (ArtistID, GenreID)
- *FK\_ArtistGenres\_Artist:* FOREIGN KEY (ArtistID) REFERENCES Artists(ID) ON DELETE CASCADE
- *FK\_ArtistGenres\_Genre:* FOREIGN KEY (GenreID) REFERENCES Genres(ID) ON DELETE CASCADE
1. **Table Name: Albums**

**○** **Description:** Хранит альбомы, выпущенные артистами.

○ **Attributes:**

- *ID:* INTEGER, PK
- *Title:* VARCHAR(150), NOT NULL
- *Release\_Year:* INTEGER
- *Cover\_URL:* TEXT

○ **Constraints:**

- *PK\_Albums:* PRIMARY KEY (id)
- *CHK\_ReleaseYear:* CHECK (release\_year > 1900)
1. **Table Name: Album\_Artists**

**○** **Description:** Связующая таблица для отношения "многие-ко-многим" между альбомами и артистами.

○ **Attributes:**

- *AlbumID:* INTEGER, PK, FK (REFERENCES Albums)
- *ArtistID:* INTEGER, PK, FK (REFERENCES Artists)
- *Is\_Primary:* BOOLEAN
- *Role:* VARCHAR(50)
- *Added\_At:* TIMESTAMP

○ **Constraints:**

- PK\_Album\_Artists: PRIMARY KEY (AlbumID, ArtistID)
- FK\_AlbumArtists\_Album: FOREIGN KEY (AlbumID) REFERENCES Albums(ID) ON DELETE CASCADE
- FK\_AlbumArtists\_Artist: FOREIGN KEY (ArtistID) REFERENCES Artists(ID) ON DELETE CASCADE
- DFT\_IsPrimary: DEFAULT FALSE
- DFT\_AddedAt: DEFAULT CURRENT\_TIMESTAMP
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
1. **Table Name: Subscription\_Types**

**○** **Description:** Справочная таблица для хранения разных типов подписок.

- *ID:* SERIAL, PK
- *Name:* VARCHAR(50), NOT NULL, UNIQUE
- *Description:* TEXT

○ **Constraints:**

- PK\_SubscriptionTypes: PRIMARY KEY (ID)
- UQ\_SubscriptionName: UNIQUE (Name)
1. **Table Name: Users**

**○** **Description:** Аккаунты слушателей.

○ **Attributes:**

- *ID:* SERIAL, PK
- *Username:* VARCHAR(50), NOT NULL
- *Email:* VARCHAR(100), NOT NULL
- *Password\_Hash:* TEXT, NOT NULL
- *Subscription\_Type\_ID:* INTEGER, FK (REFERENCES Subscription\_Types)
- *Registered\_At:* TIMESTAMP

○ **Constraints:**

- PK\_User: PRIMARY KEY (ID)
- UQ\_UserName: UNIQUE (Username)
- UQ\_UserEmail: UNIQUE (Email)
- FK\_UserSubscription: FOREIGN KEY (Subscription\_Type\_ID) REFERENCES Subscription\_Types(ID) ON DELETE SET DEFAULT
- DFT\_* SubscriptionTypeID: DEFAULT 1 –‘free’ by default
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
1. **Table Name: Playlist\_Tracks**

**○** **Description:** Техническая таблица, чтобы связывать плейлисты и треки. Один плейлист содержит много треков, один трек может быть во многих плейлистах.

○ **Attributes:** 

- *PlaylistID:* INTEGER, PK, FK (REFERENCES Playlists)
- *TrackID:* INTEGER, PK, FK (REFERENCES Tracks)
- *Track\_Order:* INTEGER, NOT NULL
- *Added\_At:* TIMESTAMP

○ **Constraints:**

- PK\_PlaylistTracks: PRIMARY KEY (PlaylistID, TrackID)
- FK\_PlaylistsTracks\_Playlist: FOREIGN KEY (PlaylistID) REFERENCES Playlists(ID) ON DELETE CASCADE
- FK\_PlaylistsTracks\_Track: FOREIGN KEY (TrackID) REFERENCES Tracks(ID) ON DELETE CASCADE
- DFT\_AddedAt: DEFAULT CURRENT\_TIMESTAMP
- CHK\_TrackOrder: CHECK (Track\_Order > 0)


**Взаимосвязи:**

● **Artists\_Genres (Многие-ко-Многим):** Один артист может иметь много жанров. Один жанр может быть у многих артистов.

○ реализована через промежуточную таблицу Artist\_Genres, где ArtistID и GenreID — внешние ключи, образующие составной первичный ключ.

● **Album\_Artists (Многие-ко-Многим):** Один альбом может иметь множество артистов Один артист может участвовать в создании множества альбомов.

○ реализована через промежуточную таблицу Album\_Artists, где AlbumID и ArtistID являются внешними ключами, образующими составной первичный ключ. Флаг Is\_Primary указывает на главного исполнителя альбома.

● **Albums и Tracks (Один-ко-Многим):** Один альбом содержит много треков. Один трек принадлежит ровно одному альбому.

○ Tracks.AlbumID является внешним ключом, ссылающимся на Albums.ID.

● **Users и Playlists (Один-ко-Многим):** Один пользователь может создать много плейлистов. Каждый плейлист создан ровно одним пользователем.

○ Playlists.UserID является внешним ключом, ссылающимся на Users.ID.

● **Playlist\_tracks (Многие-ко-Многим):** Один плейлист может содержать множество разных треков. Один трек может находиться в множестве разных плейлистов

○ реализована через промежуточную таблицу Playlist\_tracks, где PlaylistID и TrackID — внешние ключи, образующие составной первичный ключ.

