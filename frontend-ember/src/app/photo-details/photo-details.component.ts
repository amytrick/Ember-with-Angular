import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumService } from '../album.service';
import { Photo } from "../photo";

@Component({
  selector: 'app-photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.css']
})
export class PhotoDetailsComponent implements OnInit {

  photo?: Photo;

  constructor(
    private albumService: AlbumService,
    private route: ActivatedRoute
  ) { }

  getPhoto(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.albumService.getPhoto(id)
      .subscribe(photo => this.photo = photo);
  }

  ngOnInit(): void {
    this.getPhoto()
  }

}
