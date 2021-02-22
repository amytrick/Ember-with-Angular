import { TestBed } from '@angular/core/testing';

import { SharedPhotosService } from './shared-photos.service';

describe('SharedPhotosService', () => {
  let service: SharedPhotosService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SharedPhotosService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
