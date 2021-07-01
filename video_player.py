"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
       
    def show_all_videos(self, video_id,tags):
        """Returns all videos."""
        
        print("Here's a list of all available videos")
        return self._videos.get(video_id, tags)
        

        """print("show_all_videos needs implementation")"""

    def play_video(self, video_id, prev_video):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        print("play_video needs implementation")
        if prev_video: 
            print("stopping video:", str(prev_video))
            print("playing video:", str(video_id))
        else:
            print("playing video:", str(video_id))
    
        Warning(*video_id==[], "video not found")
                

    def stop_video(self,video_id):
        """Stops the current video."""

        print("stopping video:", str(video_id))
        
        if self._video_library==[]: 
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self,prev_video,video_id):
        """Plays a random video from the video library."""
        if self._video_library !=[]:
            print("stopping video:", str(prev_video))
            
        print("playing video:", str(random.choice(self._video_library)))

    def pause_video(self,video_id):
        """Pauses the current video."""
        print("video already paused", str(video_id))
        if self._video_library ==[]:
            Warning("no video is playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.pause_video==0:
            print("Cannot continue: Video is not paused")
            

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
