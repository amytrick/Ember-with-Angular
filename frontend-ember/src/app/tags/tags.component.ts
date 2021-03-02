import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../album.service';
import { SharedPhotosService } from '../shared-photos.service';
import { Tag } from '../tag';

// import { faCoffee } from '@fortawesome/free-solid-svg-icons';
// <fa-icon [icon]="faCoffee"></fa-icon>


@Component({
  selector: 'app-tags',
  templateUrl: './tags.component.html',
  styleUrls: ['./tags.component.css']
})
export class TagsComponent implements OnInit {

  tags: Tag[] = [];
  newTagword: string = "";
  public isCollapsed = true;


  constructor(
    private albumService: AlbumService,
    private sharedPhotosService: SharedPhotosService
  ) { }

  assignTag() {
    this.sharedPhotosService.assignTag(this.newTagword);
    this.isCollapsed = true;
    console.log("Assign tag");
  }

  ngOnInit(): void {
    this.sharedPhotosService.currentTags.subscribe(tags => this.tags = tags);
  }

}
