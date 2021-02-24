import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { Tag } from '../tag';

// import { faCoffee } from '@fortawesome/free-solid-svg-icons';
// <fa-icon [icon]="faCoffee"></fa-icon>


@Component({
  selector: 'app-tags',
  templateUrl: './tags.component.html',
  styleUrls: ['./tags.component.css']
})
export class TagsComponent implements OnInit {

  tags: Tag[] = []
  public isCollapsed = true;


  constructor(private albumService: AlbumService) { }

  getTags(photo_id: number): void {
    this.albumService.getTags(photo_id).subscribe(tags => this.tags = tags);
  }

  ngOnInit(): void {
    this.getTags(1);
  }

}
