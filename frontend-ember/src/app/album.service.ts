import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { Album } from './album';
import { Photo } from './photo';
import { API_URL } from './env';

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

  constructor(private http: HttpClient) { }
}
