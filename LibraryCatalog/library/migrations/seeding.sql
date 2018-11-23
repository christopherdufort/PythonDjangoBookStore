use soen341;

/*
Populate table script
This script is run manually to fill the database with demo data.
To run this script open up the mysql console and type the following command:
source absolute\path\to\seeding.sql
*/

-- one hard coded admin

TRUNCATE user;
INSERT INTO user (first_name, last_name, email, address, phone_number, is_admin, password, session_key, session_expire) VALUES ('Admin', 'Admin', 'admin@admin.com', '123admin', '1234567','1', 'admin', '', '');

-- book
TRUNCATE book;
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Java', 'R L Stine', 'Soft Cover', 100, 'Clearing House', 'English', 1023456789, 1023456789100);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Sql', 'G K Chesterton', 'Hard Cover', 129, 'Clearing House', 'English', 1322222111, 220888877889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Python', 'R L Stine', 'Soft Cover', 158, 'Clearing House', 'English', 899988989, 997998911011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Books of Magic', 'Neil Gaiman', 'Hard Cover', 187, 'Clearing House', 'English', 9098909911, 881892190089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Childrens Crusade', 'Neil Gaiman', 'Soft Cover', 216, 'Clearing House', 'English', 792081189, 207326818811);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Good Omens', 'R L Stine', 'Hard Cover', 245, 'Clearing House', 'English', 8416037711, 595355062289);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('InterWorld', 'Michael Reaves', 'Soft Cover', 274, 'ABC Books', 'English', 3187733389, 770151166611);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Silver Dream', 'Carl Sagan', 'Hard Cover', 303, 'ABC Books', 'English', 5585605511, 554965494489);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Ocean at the End of the Lane', 'Carl Sagan', 'Soft Cover', 332, 'ABC Books', 'English', 2974945589, 491583954411);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Anansi Boys', 'Mallory Reaves', 'Hard Cover', 361, 'ABC Books', 'English', 4519613311, 956811486689);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Last Temptation', 'Carl Sagan', 'Soft Cover', 390, 'ABC Books', 'English', 7441717789, 164337182211);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Miracleman', 'Carl Sagan', 'Hard Cover', 419, 'ABC Books', 'English', 6730061111, 999381038889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Creatures of the Night', 'Mark Twain', 'Soft Cover', 448, 'ABC Books', 'English', 6276049989, 598722850011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Children of Men', 'P. D. James', 'Hard Cover', 477, 'ABC Books', 'English', 1328948911, 893562151089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Cricket on the Hearth', 'Charles Dickens', 'Soft Cover', 506, 'ABC Books', 'English', 1565942189, 592652957811);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('For a Breath I Tarry', 'Roger Zelazny', 'Hard Cover', 535, 'ABC Books', 'English', 5028276711, 822642823289);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The House of Mirth', 'Jessica Anderson', 'Soft Cover', 564, 'ABC Books', 'English', 7799394389, 931639505611);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('In Death Ground', 'Mark Twain', 'Hard Cover', 593, 'ABC Books', 'English', 2140044511, 2311055489);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Little Foxes', 'Lewis Carol', 'Soft Cover', 622, 'Golden books', 'English', 1864406589, 438794493411);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Moon by Night', 'Lewis Carol', 'Hard Cover', 651, 'Golden books', 'English', 4576252311, 620654847689);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('A Passage to India', 'Humphrey Cobb', 'Soft Cover', 680, 'Golden books', 'English', 3048978789, 894829921211);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('That Hideous Strength', 'George Orwell', 'Hard Cover', 709, 'Golden books', 'English', 1848900111, 888162199889);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('Unweaving the Rainbow', 'Stephen King', 'Soft Cover', 738, 'Golden books', 'English', 3041110989, 108057789011);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('The Wives of Bath', 'Stephen Gray', 'Hard Cover', 767, 'Golden books', 'English', 1069987911, 997721112089);
INSERT INTO book (title, author, format, pages, publisher, language, isbn_10, isbn_13) VALUES ('A Time of Gifts', 'Stephen King', 'Soft Cover', 796, 'Golden books', 'English', 5928803189, 874390096811);

-- magazine
TRUNCATE magazine;
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Alive Magazine', 'Teldon Publishing', 'English', 9012345678, 9012345678912);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Auto Atlantic', 'Robert Alfers', 'English', 2222222122, 219989977878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Canada World View', 'Readers Digest', 'English', 9999990078, 989007809922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Canadian Dimension', 'St. Joseph Media', 'English', 9999017722, 891773182278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Chickadee', 'Readers Digest', 'English', 9902754478, 265545045522);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Checkerspot', 'Black Angus Media', 'French', 372693322, 268959506678);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Downhome', 'Lifestyle', 'English', 6896638878, 656991161122);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Fuse', 'Arts and culture', 'English', 2767248922, 722124951078);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('HighGrader', 'Rural lifestyle and culture', 'English', 3957643278, 760370156722);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Justice Magazine', 'True crime', 'English', 1806684522, 666645515478);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Literary Review of Canada', 'Literary', 'English', 8861767678, 167906032322);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('The Magazine', 'Magazines 2000', 'English', 7315000122, 492697199878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Music Express', 'Life Media', 'French', 4185012078, 497022787922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('The New Quarterly', 'Magazines 2000', 'English', 4316195722, 615256004278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('The Nerve', 'Magazines 2000', 'English', 7303376478, 330344423522);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Nightlife', 'Black Angus Media', 'French', 3034271322, 424097928678);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Opera Canada', 'Life Media', 'English', 392860878, 285694939122);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Peace Magazine', 'Rogers Media', 'English', 8893226922, 313798973078);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Rites', 'Readers choice', 'English', 429465278, 946098334722);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Rue Morgue', 'Great River Media', 'English', 2517062522, 703735137478);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('People 21', 'Readers choice', 'English', 9189189678, 909778610322);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Sports Illustrated Vol 22', 'Readers choice', 'English', 9729778122, 968082421878);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Spacing', 'Readers choice', 'English', 3248034078, 800159765922);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Times Vol 24', 'Great River Media', 'Multi', 1555373722, 535816826278);
INSERT INTO magazine (title, publisher, language, isbn_10, isbn_13) VALUES ('Toronto Life', 'Rogers Media', 'English', 3981998478, 195865801522);

-- video
TRUNCATE video;
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('The Lazy song', 'Luis Fonsi', 'Daddy Yankee', 'Ed Sheeran', 'Descemer Bueno', 'English', 'French', '2017-11-02', '5 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Let it go', 'Wiz Khalifa', 'Charlie Puth', 'Mark Ronson', 'Bruno Mars', 'English', 'French', '2009-11-04', '21 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Treat You Better', 'Psy', 'Justin Bieber', 'Maroon', 'Gente De Zona', 'English', 'French', '2006-11-09', '36 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Worth It', 'Taylor Swift', 'Katy Perry', 'Enrique Iglesias', 'Hunter S Thompson', 'English', 'French', '1998-11-03', '50 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Rude', 'Ed Sheeran', 'OneRepublic', 'Katy Perry', 'Juicy J', 'English', 'French', '1990-11-12', '4 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('New Rules', 'Major Lazer', 'DJ Snake', 'Adele', 'Thompson', 'English', 'French', '2000-11-09', '5 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Rolling in the Deep', 'Taylor Swift', 'Maluma', 'Meghan Trainor', 'Thompson', 'English', 'French', '2011-11-29', '10 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Side to Side', 'Halsey', 'Passenger', 'LittleBabyBum', 'Hunter', 'English', 'French', '2013-11-12', '8 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Something Just like This', 'Rihanna', 'J Balvin', 'Willy William', 'Freshlyground', 'English', 'French', '2015-11-20', '9 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('All of Me', 'Shakira', 'Freshlyground', 'Producer Walker', 'Ludacris', 'English', 'French', '2018-11-31', '20 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('On the Floor', 'Charlie Puth', 'Selena Gomez', 'Clean Bandit', 'Hunters', 'English', 'French', '2009-11-22', '43 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Burn', 'Sia', 'Ellie Goulding', 'Avicii', 'Demi Lovato', 'English', 'French', '2004-11-13', '2 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('The Hills', 'Rihanna', 'Natti Natasha ', 'Ozuna', 'Hunter S Thompson', 'English', 'French', '1996-11-10', '44 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Diamonds', 'Kid Ink', 'Adele', 'Drake', 'Shakira', 'English', 'French', '2011-11-22', '22 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Bang Bang', 'Ryan ToysReview', 'Lamar', 'Manuel Turizo', 'Pulcino Pio', 'English', 'French', '2001-11-10', '33 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Bad Blood', 'Shawn Mendes', 'Mars', 'Sana', 'Montana', 'English', 'French', '2011-11-12', '21 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Summer', 'Idina Menzel', 'Harris', 'Annana', 'Psy', 'English', 'French', '2000-11-11', '31 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Animals', 'Ed Sheeran', 'Calvin', Peirl', 'Adele', 'English', 'French', '2000-11-13', '12 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Picky', '	Silentó', 'Guetta', 'Ocean', 'Sean Paul', 'English', 'French', '2001-11-01', '11 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('GentleMan', 'GoonRock', 'Minaj', 'Afrojack', 'Ty Dolla Sign', 'English', 'French', '2011-11-09', '10 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Don't Let Me Down', 'Dua Lipa', 'Soer', 'Deanin', 'terson', 'English', 'French', '2005-11-09', '8 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Not Afraid', 'J Balvin', 'over', 'Wanz', 'Nicki Minaj', 'English', 'French', '2018-11-12', '2 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Swalla', 'Bruno Mars', 'Daddy Yankee', 'Rihanna', 'Disciples', 'English', 'French', '2018-11-12', '31 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Havana', 'Maluma', 'The Weeknd', 'Cardi B', 'Ellie Goulding', 'English', 'French', '2018-11-12', '50 minutes');
INSERT INTO video (title, director, producers, actors, language, subtitles, dubbed, release_date, run_time) VALUES ('Axel', 'Crazy Frog', 'Ozuna', 'Nicky Jam', 'Daddy Yankee', 'English', 'French', '2018-11-12', '98 minutes');

-- music
TRUNCATE music;
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Desire 126', 'cd', 'Hollerado', 'English', '1992-06-04', 45678910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Earth Air Water Trees', 'casette', 'The Mountain Goats', 'English', '1990-12-04', 33231090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Harpeur', 'vinyl record', 'Led Zeppelin', 'English', '1950-04-02', 97858910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Homa', '8 track', 'Peter Peter', 'English', '2000-03-18', 61051090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('La Stakose', 'cd', 'Mes Aieux', 'English', '2010-02-22', 90038910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Your Precious Love', 'casette', 'Led Zeppelin', 'French', '2011-03-04', 48871090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Ain't Nothing Like the Real Thing', 'vinyl record', 'Pink Floyd', 'English', '1993-06-22', 22218910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('I Am Your Man', '8 track', 'Vancouvers', 'French', '1992-06-04', 96691090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Remember Me', 'cd', 'Burt Bacharach', 'English', '1999-06-04', 94398910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Let the Spirit Descend', 'casette', 'Pink', 'English', '2000-02-10', 4511090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Fortunate Son', 'vinyl record', 'Creedence Clearwater Revival', 'English', '1999-08-29', 6578910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('The Beatles', '8 track', 'Pink Floyd', 'English', '1995-02-25', 72331090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Let It Be', 'cd', 'Neil Young', 'French', '1991-05-08', 58758910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Abbey Road', 'casette', 'Kim Jong-hyun', 'English', '1999-04-04', 151090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Rubber Soul', 'vinyl record', 'Norman Whitfield', 'English', '1991-02-04', 50938910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Please Please Me', '8 track', 'Super Junior', 'English', '1996-02-05', 87971090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Love', 'cd', 'Neil Young', 'English', '1991-03-03', 83118910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Revolver', 'casette', 'Frank Ocean', 'Japaneese', '1992-04-02', 35791090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Single', 'vinyl record', 'Metallica', 'English', '1992-03-02', 55298910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Taxman', '8 track', 'Dottie Rambo', 'English', '1990-02-02', 43611090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Yellow Submarine', 'cd', 'Curtis Mayfield', 'English', '1989-03-04', 67478910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Rubber Soul', 'casette', 'Metallica', 'Kannada', '2015-08-17', 11431090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('Lovely Rita', 'vinyl record', 'Rock Band', 'English', '2010-08-04', 19658910);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('You Won't See Me', '8 track', 'Revolution X', 'English', '2000-09-04', 39251090);
INSERT INTO music (title, type, artist, label, release_date, ASIN) VALUES ('In My Life', 'cd', 'Rock Band', 'English', '2010-10-04', 11838910);
