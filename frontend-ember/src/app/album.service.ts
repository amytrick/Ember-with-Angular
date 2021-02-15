import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';

import { Album } from './album';
import {API_URL} from './env';

@Injectable({
  providedIn: 'root'
})
export class AlbumService {
  private albumsUrl = `${API_URL}/get_albums`

  getAlbums(user_id: number): Observable<Album[]> {
    const url = `${this.albumsUrl}/${user_id}`
    return this.http.get<Album[]>(url);
  }

  constructor(private http: HttpClient) { }
}
