'''Contains classes which store information about movies and tv series.'''
import webbrowser


class Video():
    '''Contains information about videos.
    Parent of classes Movie and Tv_series.
    '''
    def __init__(self, storyline, video_url):
        '''Creates instances of videos'''
        self.storyline = storyline
        self.video_url = video_url

    def show_video(self):
        '''Opens video with given url in the web browser.'''
        webbrowser.open(self.video_url)


class Movie(Video):
    '''Contains information about movies.'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''Creates instances of type movies'''
        Video.__init__(self, movie_storyline, trailer_youtube)
        self.title = movie_title
        self.poster_image_url = poster_image


class Tv_series(Video):
    '''Contains information about Tv series.'''
    def __init__(self, series_title, series_season, series_storyline,
                 episode_image, episode_url):
        '''Creates instances of type tv series'''
        Video.__init__(self, series_storyline, episode_url)
        self.title = series_title
        self.poster_image_url = episode_image
        self.title += ' ' + 'season-' + series_season
