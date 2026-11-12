/******************************************************************************
 **
 ** File      SimpleMediaApiWrapper.js
 ** Author    Maksym Aldokhin
 ** Copyright (c) 2026, Corsair Memory, Inc. All Rights Reserved.
 **
 ** This file is part of Corsair iCUE Software.
 **
 ******************************************************************************/

/**
 * Media API
 *
 * Media-specific wrapper that extends IcueWidgetApiWrapper.
 * Provides convenient methods for sensor data retrieval.
 *
 * For initialization use mediaplugin.
 *
 * Usage:
 *   const api = new SimpleMediaApiWrapper(mediaplugin);
 *   api.getSongName().then(value => {
 *       console.log("Song name value:", value);
 *   });
 *   api.getArtist().then(value => {
 *       console.log("Artist value:", value);
 *   });
 *   api.getAlbum().then(value => {
 *       console.log("Album value:", value);
 *   });
 *   api.getThumbnail().then(value => {
 *       console.log("Thumbnail data URL:", value);
 *   });
 *   api.getIsPlaying().then(value => {
 *       console.log("Is playing:", value);
 *   });
 */

class SimpleMediaApiWrapper extends IcueWidgetApiWrapper {
	constructor(mediaPlugin, timeoutMs = 5000) {
		super(mediaPlugin, timeoutMs);
	}

	getSongName() {
		return this.request(this.plugin.getSongName);
	}

	getArtist() {
		return this.request(this.plugin.getArtist);
	}

	getThumbnail() {
		return this.request(this.plugin.getThumbnail);
	}

	getAlbum() {
		return this.request(this.plugin.getAlbum);
	}

	getIsPlaying() {
		return this.request(this.plugin.getIsPlaying);
	}
}
