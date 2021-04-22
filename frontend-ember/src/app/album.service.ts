import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { Album } from './album';
import { Photo } from './photo';
import { Tag } from './tag';
import { API_URL } from './env';

import { Cloudinary } from '@cloudinary/angular-5.x';


@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  private albumsUrl = `${API_URL}/get-albums`

  getAlbums(user_id: number): Observable<Album[]> {
    const url = `${this.albumsUrl}/${user_id}`
    return this.http.get<Album[]>(url);
  }

  getPhotos(album_id: number): Observable<Photo[]> {
    const url = `${API_URL}/get-photos/album/${album_id}`
    return this.http.get<Photo[]>(url);
  }

  getAlbum(album_id: number): Observable<Album> {
    const url = `${API_URL}/get-album/${album_id}`
    return this.http.get<Album>(url);
  }

  getPhoto(photo_id: number): Observable<Photo> {
    const url = `${API_URL}/get-photo/${photo_id}`
    return this.http.get<Photo>(url);
  }

  fillLibrary(user_id: number): Observable<Photo[]> {
    const url = `${API_URL}/library/${user_id}`
    return this.http.get<Photo[]>(url);
  }

  getTags(photo_id: number): Observable<Tag[]> {
    const url = `${API_URL}/get-tags/${photo_id}`
    return this.http.get<Tag[]>(url);
  }

  addAlbum(name: string, user_id: number): Observable<Album> {
    return this.http.post<Album>(`${API_URL}/add-album`, { name: name, user_id: user_id, datetime: Date.now() });
  }

  uploadPhoto(photo_base64: string): void {
    console.log("Trying to make post request to upload photo");
    this.http.post(`${API_URL}/upload-photo`, { photo_base64: photo_base64 }).subscribe();
  }

  setFilter(currentRating: Number, equality: string, album_id: number): Observable<Photo[]> {
    console.log("Post request of filtered rating")
    return this.http.post<Photo[]>(`${API_URL}/filter`, { equality: equality, rating: currentRating, user_id: 1, album_id: album_id });
  }

  search(searchword: string): Observable<Photo[]> {
    console.log("Post request of searchword")
    return this.http.post<Photo[]>(`${API_URL}/search`, { searchword: searchword, user_id: 1 });
  }

  constructor(
    private http: HttpClient,
    private cloudinary: Cloudinary
  ) { }
}
