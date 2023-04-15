CREATE TABLE `Song` (
  `id` integer PRIMARY KEY,
  `name` varchar(30),
  `author_id` integer,
  `album_id` integer
);

CREATE TABLE `Album` (
  `id` integer PRIMARY KEY,
  `name` varchar(30),
  `author_id` integer,
  `songs` Ref
);

CREATE TABLE `Author` (
  `id` integer PRIMARY KEY,
  `name` varchar(40),
  `birth_date` datetime
);

CREATE TABLE `AuthorSong` (
  `author_id` integer,
  `song_id` integer
);

ALTER TABLE `Song` ADD FOREIGN KEY (`author_id`) REFERENCES `Author` (`id`);

ALTER TABLE `Song` ADD FOREIGN KEY (`album_id`) REFERENCES `Album` (`id`);

ALTER TABLE `Album` ADD FOREIGN KEY (`author_id`) REFERENCES `Author` (`id`);

-- CREATE TABLE `Song_AuthorSong` (
--   `Song_id` integer,
--   `AuthorSong_song_id` integer,
--   PRIMARY KEY (`Song_id`, `AuthorSong_song_id`)
-- );

-- ALTER TABLE `Song_AuthorSong` ADD FOREIGN KEY (`Song_id`) REFERENCES `Song` (`id`);

-- ALTER TABLE `Song_AuthorSong` ADD FOREIGN KEY (`AuthorSong_song_id`) REFERENCES `AuthorSong` (`song_id`);


-- CREATE TABLE `Author_AuthorSong` (
--   `Author_id` integer,
--   `AuthorSong_author_id` integer,
--   PRIMARY KEY (`Author_id`, `AuthorSong_author_id`)
-- );

-- ALTER TABLE `Author_AuthorSong` ADD FOREIGN KEY (`Author_id`) REFERENCES `Author` (`id`);

-- ALTER TABLE `Author_AuthorSong` ADD FOREIGN KEY (`AuthorSong_author_id`) REFERENCES `AuthorSong` (`author_id`);

