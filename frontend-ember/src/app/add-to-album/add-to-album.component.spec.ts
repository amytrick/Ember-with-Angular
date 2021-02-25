import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddToAlbumComponent } from './add-to-album.component';

describe('AddToAlbumComponent', () => {
  let component: AddToAlbumComponent;
  let fixture: ComponentFixture<AddToAlbumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddToAlbumComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddToAlbumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
